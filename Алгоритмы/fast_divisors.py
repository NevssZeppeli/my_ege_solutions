# Все возможные делители числа (для больших чисел)
# Это НЕ ТОЛЬКО разложение на простые множители
import itertools
 
def get_factorization(x: int) -> list:
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
 
x = int(input())
x_factors = get_factorization(x)
#print(x_factors)
 
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
print(all_divisors)
