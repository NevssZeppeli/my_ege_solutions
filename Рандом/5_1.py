def f(n):
    r = ''
    z = 0
    e = 0
    y = bin(n)[2:]
    print(y)
    for x in y:
        if x == '0':
            z+=1
        if x == '1':
            z+=1
    if e > z:
        y + '0'
    else:
        y + '1'

    return y

for k in range(50, 100+1):
    print(f(k))