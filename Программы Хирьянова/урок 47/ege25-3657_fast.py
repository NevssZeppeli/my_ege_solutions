# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3657
# [1000000; 1300000]
# все цифры меньше 3, а сумма цифр кратна 10
# отобрать каждое десятое в порядке возрастания,
# справа укажите кол-во его собственных делителей
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


A = []
for x in range(1000000, 1300000+1):
    if (all(digit in "012" for digit in str(x)) and
        sum(int(digit) for digit in str(x)) % 10 == 0):
        A.append(x)
B = A[9::10]  # каждое десятое число
for x in B:
    num_divs = len(get_divisors(x)) - 2
    print(x, num_divs)
