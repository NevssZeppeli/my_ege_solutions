count = 0
for y in range(1, 10000000):
    x = y
    a = 0
    b = 0
    while x > 0:
        a = a + 1
        if x % 2 != 0:
            b = b+1
        x = x//2
    if a == 16 and b == 14:
        count+=1
        print(a,b)

print(count)

