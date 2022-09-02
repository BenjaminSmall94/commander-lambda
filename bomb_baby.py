# This function is for optimization. For very large input it determines if the function is
# solvable in Log2(n) of time (it always cuts the largest number at least by a factor of 2
# It turns out this is Euclid's algorithm for finding the greatest common denominator.
# I actually just realized the pattern by writing out the first dozen or so iterations.
# https://protonstalk.com/basic-math/coprime-numbers/#:~:text=Two%20numbers%20are%20Coprimes%20if,HCF(Highest%20Common%20Factor).
def solution(x, y):
    num_generations = 0
    x = int(x)
    y = int(y)
    if not are_coprime(x, y):
        return "impossible"
    while x >= 1 and y >= 1:
        if x == 1 and y == 1:
            return str(int(num_generations))
        else:
            if x > y:
                difference = x - y
                if y == 1:
                    reps = difference / y
                else:
                    reps = difference / y + 1
                x -= reps * y
                num_generations += reps
            else:
                difference = y - x
                if x == 1:
                    reps = difference / x
                else:
                    reps = difference / x + 1
                y -= reps * x
                num_generations += reps
    return "impossible"

def are_coprime(x, y):
    if x == 1 or y == 1:
        return True
    elif x == 0 or y == 0:
        return False
    else:
        if x > y:
            return are_coprime(x % y, y)
        else:
            return are_coprime(x, y % x)




if __name__ == "__main__":
    print(solution('66', '25'))
    print(are_coprime(66, 25))