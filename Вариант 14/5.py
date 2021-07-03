def f(n):
    e = 0
    y = bin(n)[2::]
    y += y[-1]
    for symb in y:
        if symb == '1':
            e +=1
    if e % 2 == 0:
        y += '00'
    else:
        y += '10'
    return int(y,2)

for k in range(1, 50):
    if f(k) > 114:
        print(k)
        break