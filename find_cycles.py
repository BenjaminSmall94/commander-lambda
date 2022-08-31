def solution(n, b):
    encountered_nums = []
    return find_IDs(n, b, encountered_nums)


def find_IDs(n, b, encountered_nums):
    if n in encountered_nums:
        return len(encountered_nums) - encountered_nums.index(n)
    encountered_nums.append(n)
    x = ''.join(sorted(n, reverse=True))
    y = ''.join(sorted(n))
    x_num = to_base10(x, b)
    y_num = to_base10(y, b)
    z_num = x_num - y_num
    z = to_baseB(z_num, b, len(n) - 1)
    return find_IDs(z, b, encountered_nums)


def to_base10(n, b):
    num_sum = 0
    for i in range(len(n)):
        num_sum += int(n[len(n) - 1 - i]) * b ** i
    return num_sum


def to_baseB(num, base, k):
    num_str = ''
    for i in range(k, -1, -1):
        quotient = num // base ** i
        num_str += str(quotient)
        num = num - quotient * base ** i
    return num_str


print(solution('210022', 3))
