# I had to review my matrix Algebra. I took a class on it 8 years ago. Take a look at my previous
# solution for my attempt without determinants. That solution was passing 7/10 tests. I switched
# my approach and researched as much as possible and with the help of my research I came up with this solution.

def solution(m):
    terminal_states = []
    non_terminal_states = []
    markov_matrix = []
    for row_idx, row in enumerate(m):
        row_sum = sum(row)
        if row_sum == 0:
            terminal_states.append(row_idx)
        else:
            non_terminal_states.append(row_idx)
        markov_row = []
        for col in row:
            if col == 0:
                markov_row.append((col, 1))
            else:
                gcd = find_gcd(col, max(row_sum, 1))
                markov_row.append((col / gcd, max(row_sum, 1) / gcd))
        markov_matrix.append(markov_row)
    if terminal_states[0] == 0:
        output = [1]
        for _ in range(1, len(terminal_states)):
            output.append(0)
        output.append(1)
        return output
    r_matrix, q_matrix = get_rq(markov_matrix, terminal_states, non_terminal_states)
    identity = make_identity_matrix(len(q_matrix))
    identity_q = subtract_matrices(identity, q_matrix)
    i_q_inverse = get_inverse(identity_q)
    iqi_r = mulitply_matrix(i_q_inverse, r_matrix)
    return format_answer(iqi_r[0])



def get_inverse(matrix):
    inverse = []
    n = len(matrix)
    for row in range(n):
        numerator_row = []
        for column in range(n):
            sub_matrix = get_sub_matrix(matrix, row, column)
            determinant = get_determinant(sub_matrix)
            numerator_row.append(multiply_fractions(((-1)**(row + column), 1), determinant))
        inverse.append(numerator_row)
    total_determinant = get_determinant(matrix)
    inverse = get_transpose(inverse)
    for i in range(len(inverse)):
        for j in range(len(inverse[i])):
            inverse[i][j] = multiply_fractions(inverse[i][j], (total_determinant[1], total_determinant[0]))
    return inverse


def get_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return add_fractions(multiply_fractions(matrix[0][0], matrix[1][1]), multiply_fractions((-1,1), multiply_fractions(matrix[0][1], matrix[1][0])))

    determinant = (0, 1)
    for col_idx in range(len(matrix[0])):
        sub_matrix = get_sub_matrix(matrix, 0, col_idx)
        determinant = add_fractions(determinant, multiply_fractions(multiply_fractions(((-1) ** col_idx, 1), matrix[0][col_idx]), get_determinant(sub_matrix)))


    return determinant


def get_sub_matrix(matrix, i, j):
    sub_matrix = []
    for row in matrix[:i] + matrix[i + 1:]:
        sub_matrix_row = []
        for num in row[:j] + row[j + 1:]:
            sub_matrix_row.append(num)
        sub_matrix.append(sub_matrix_row)
    return sub_matrix


def get_transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def mulitply_matrix(A, B):
    result = []
    for row in range(len(A)):
        result_row = []
        for column in range(len(B[0])):
            sum_products = (0, 1)
            for mult_index in range(len(A)):
                sum_products = add_fractions(sum_products, multiply_fractions(A[row][mult_index], B[mult_index][column]))
            result_row.append(sum_products)
        result.append(result_row)
    return result


def get_rq(markov, terminal, non_terminal):
    r = []
    q = []
    for row in non_terminal:
        r_row = []
        q_row = []
        for col in terminal:
            r_row.append(markov[row][col])
        for col in non_terminal:
            q_row.append(markov[row][col])
        r.append(r_row)
        q.append(q_row)
    return r, q


def make_identity_matrix(n):
    identity = [[(0, 1) for _ in range(n)] for __ in range(n)]
    for idx in range(n):
        identity[idx][idx] = (1, 1)
    return identity


def subtract_matrices(a, b):
    result = []
    n = len(a)
    for i in range(n):
        row = []
        for j in range(n):
            row.append(add_fractions(a[i][j], multiply_fractions((-1, 1), b[i][j])))
        result.append(row)
    return result


def format_answer(probabilities):
    lcm = 1
    for probability in probabilities:
        lcm = find_lcm(lcm, probability[1])
    output = []
    for probability in probabilities:
        multiplicand = lcm / probability[1]
        output.append(int(probability[0] * multiplicand))
    output.append(int(lcm))
    return output


def add_fractions(a, b):
    lcm = find_lcm(a[1], b[1])
    a_multiplicand = lcm / a[1]
    b_multiplicand = lcm / b[1]
    dividend = a[0] * a_multiplicand + b[0] * b_multiplicand
    gcd = find_gcd(dividend, lcm)
    return dividend / gcd, lcm / gcd


def multiply_fractions(a, b):
    dividend = a[0] * b[0]
    divisor = a[1] * b[1]
    gcd = find_gcd(dividend, divisor)
    return dividend / gcd, divisor / gcd


def find_gcd(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return find_gcd(a % b, b)
        else:
            return find_gcd(a, b % a)


def find_lcm(a, b, gcd=None):
    if gcd is None:
        gcd = find_gcd(a, b)
    return a * b / gcd


if __name__ == "__main__":
    # y = [[0, 1, 0, 0, 0, 1],
    #      [4, 0, 0, 3, 2, 0],
    #      [0, 0, 0, 0, 0, 0],
    #      [0, 0, 0, 0, 0, 0],
    #      [0, 0, 0, 0, 0, 0],
    #      [0, 0, 0, 0, 0, 0]]

    # y = [[0, 2, 1, 0, 0],
    #     [0, 0, 0, 3, 4],
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0]]

    # a = [[0, 1, 830, 927],
    #      [0, 1, 14325, 555],
    #      [0, 0, 0, 0],
    #      [0, 0, 0, 0]]
    #
    z = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 99, 22, 1, 23, 59],
         [1, 1, 0, 0, 1, 101, 1, 597, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print(solution(z))

    # [824315, 919621, 1743936]
    # [450404, 502479, 952883]

    # x = [[0, 1, 0, 0, 1],
    #      [0, 2, 0, 0, 1],
    #      [0, 0, 0, 1, 1],
    #      [0, 0, 0, 0, 1],
    #      [0, 0, 0, 0, 0]]
