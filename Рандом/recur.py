def f(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return f(n/2) + 1
    if n >= 2 and n % 2 != 0:
        return f(n*3 + 1) + 1

def rec():
    count = 0
    for x in range(1, 100 + 1):
        if (f(x)) > 100:
            count += 1
            print(x)
    print("кол-во:", count)

rec()