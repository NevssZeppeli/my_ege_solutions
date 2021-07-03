# Все возможные делители числа (для больших чисел)
# Это НЕ ТОЛЬКО разложение на простые множители
def get_factors(x: int) -> list:
    factors = []
    d = 2
    while x >= d*d:
        if x % d == 0:
            factors.append(d)
            x //= d
        else:
            d += 1
    factors.append(x)
    return factors


def get_divisors(x):
    x_factors = get_factors(x)
    all_divisors = []
    for selector in range(2**len(x_factors)):
        divisor = 1
        for i in range(len(x_factors)):
            digit = selector % 2  # last digit in binary base
            if digit == 1:  # used digit to get factor (or not)
                divisor *= x_factors[i]
            selector //= 2  # throw out the last digit
        all_divisors.append(divisor)
    all_divisors = sorted(set(all_divisors))  # kill siblings
    return all_divisors


x = int(input())
print(get_divisors(x))




