n = 0
for y in range(10000):
    x = y
    a = 0 
    b = 0
    while x > 0: 
        a = a + 1
        b = b + (x % 10)
        x = x // 10
    if a == 2 and b == 12:
        print(y)
        n += 1

print(n)
