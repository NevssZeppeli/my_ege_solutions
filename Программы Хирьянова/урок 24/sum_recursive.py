def sum_input(n: int):
    if n == 0:
        result = 0
    elif n < 0:
        result = None
    else:
        x = int(input())
        result = x + sum_input(n - 1)
    return result

print(sum_input(5))

def summ(n: int):
    # assert n >= 0, "Never should be called with negative numbers"
    return 0 if n == 0 else int(input()) + summ(n - 1)

