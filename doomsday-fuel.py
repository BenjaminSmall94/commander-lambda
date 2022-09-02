def solution(m):
    rows_denom = {}
    terminal_states = {}
    for idx, row in enumerate(m):
        row_sum = sum(row)
        rows_denom[idx] = row_sum
        if row_sum == 0:
            terminal_states[idx] = (0, 1)
    if terminal_states.get(0):
        output = [1]
        for _ in range(1, len(terminal_states)):
            output.append(0)
        output.append(1)
        return output
    probabilities = find_probabilities(m, 0, terminal_states, rows_denom, (1, 1))
    return format_probs(probabilities)


def find_probabilities(m, row, terminal_states, rows_denom, prob):
    for row_idx, num in enumerate(m[row]):
        if num > 0:
            if row_idx in terminal_states:
                terminal_states[row_idx] = add_fractions(terminal_states[row_idx], (prob[0] * num, prob[1] * rows_denom[row]))
                # terminal_states[row_idx] = (prob[0] * num, prob[1] * rows_denom[row])
            else:
                find_probabilities(m, row_idx, terminal_states, rows_denom, (prob[0] * num, prob[1] * rows_denom[row]))
    return terminal_states


def format_probs(probs):
    lcm = 1
    for value in probs.values():
        lcm = find_lcm(lcm, value[1])
    output = []
    for key, value in probs.items():
        multiplicand = lcm / value[1]
        output.append(value[0] * multiplicand)
    output.append(lcm)
    return output


def add_fractions(a, b):
    lcm = find_lcm(a[1], b[1])
    a_multiplicand = lcm / a[1]
    b_multiplicand = lcm / b[1]
    dividend = a[0] * a_multiplicand + b[0] * b_multiplicand
    gcd = find_gcd(dividend, lcm)
    return dividend / gcd, lcm / gcd


def find_gcd(a, b):
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
    x = [[0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1]]

    print(solution(x))
    test_cases = False
    if test_cases:
        y = [[0, 1, 0, 0, 0, 1],
             [4, 0, 0, 3, 2, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
