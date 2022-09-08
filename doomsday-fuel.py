def solution(m):
    terminal_states = []
    transition_matrix = []
    for row_idx, row in enumerate(m):
        row_sum = sum(row)
        if row_sum == 0:
            terminal_states.append(row_idx)
        transition_row = []
        for col_idx, col in enumerate(row):
            if col == 0:
                transition_row.append((col, 1))
            else:
                transition_row.append((col, max(row_sum, 1)))
            if row_idx == col_idx:
                transition_row[col_idx] = add_fractions((-1, 1), transition_row[col_idx])
        transition_matrix.append(transition_row)
    if terminal_states[0] == 0:
        output = [1]
        for _ in range(1, len(terminal_states)):
            output.append(0)
        output.append(1)
        return output
    probabilities = {}
    for row_idx in terminal_states:
        probabilities[row_idx] = (find_probabilities(transition_matrix, row_idx))
    return format_answer(probabilities)


def find_probabilities(transition_matrix, end_row_idx):
    matrix_copy = [[col_val for col_val in row] for row in transition_matrix]
    size = len(matrix_copy)
    for i in range(size):
        if i == end_row_idx:
            matrix_copy[i].append((1, 1))
        else:
            matrix_copy[i].append((0, 1))
    for row_idx in range(size - 1, -1, -1):
        if matrix_copy[row_idx][row_idx] != (-1, 1):
            make_negative_one(matrix_copy[row_idx], row_idx, size)
        for row in range(size):
            if row != row_idx:
                multiplicand = matrix_copy[row][row_idx]
                for col_idx in range(size):
                    matrix_copy[row][col_idx] = add_fractions(matrix_copy[row][col_idx], multiply_fractions(multiplicand, (matrix_copy[row_idx][col_idx])))
                matrix_copy[row][size] = add_fractions(matrix_copy[row][size], multiply_fractions(multiplicand, (matrix_copy[row_idx][size])))
    return matrix_copy[0][size]
# 830 / 1758

def format_answer(probs):
    lcm = 1
    for value in probs.values():
        lcm = find_lcm(lcm, value[1])
    output = []
    for key, value in probs.items():
        multiplicand = lcm / value[1]
        output.append(int(value[0] * multiplicand))
    output.append(int(lcm))
    return output


def make_negative_one(matrix_row, idx, size):
    value = matrix_row[idx]
    if value[0] > 0:
        multiplicand = (-1 * value[1], value[0])
    else:
        multiplicand = (value[1], -1 * value[0])
    for col_idx in range(idx + 1):
        matrix_row[col_idx] = multiply_fractions(multiplicand, (matrix_row[col_idx]))
    matrix_row[size] = multiply_fractions(multiplicand, (matrix_row[size]))


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

    a = [[0, 1, 830, 927],
         [0, 1, 14325, 555],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

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
    sol = solution(a)
    print(sol)
    print(sum(sol[:-1]))
    print(sol[len(sol) - 1])

    # [824315, 919621, 1743936]
    # [450404, 502479, 952883]

    # x = [[0, 1, 0, 0, 1],
    #      [0, 2, 0, 0, 1],
    #      [0, 0, 0, 1, 1],
    #      [0, 0, 0, 0, 1],
    #      [0, 0, 0, 0, 0]]
