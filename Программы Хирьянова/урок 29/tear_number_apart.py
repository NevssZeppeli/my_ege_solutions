n, s, p = 0, 0, 1
x = int(input())
while x != 0:
    digit = x % 10  # взять последнюю цифру в 10-й СС
    if digit % 2 == 1:  # если цифра нечётная, то
        n += 1
        s += digit
        p *= digit
    x = x // 10  # x //= 10 -- отбросить последнюю цифру
print(n, s, p)
