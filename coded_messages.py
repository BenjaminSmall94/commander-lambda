def solution(l, t):
    left_bound = 0
    set_sum = 0
    for right_bound in range(len(l)):
        set_sum += l[right_bound]
        while set_sum > t:
            set_sum -= l[left_bound]
            left_bound += 1
        if set_sum == t:
            return [left_bound, right_bound]
    return [-1, -1]


print(solution([4, 3, 10, 2, 8], 12))
