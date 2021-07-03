def f(n: str):
    x = bin(n)[2::]
    print(x)
    x += x[-1]
    if x.count('1') % 2 == 0:
        x += '0'
    else:
        x += '1'
    if x.count('1') % 2 == 0:
        x+='0'
    else:
        x+='1'
    print(int(x,2))
    return x
    #if y.count('1') % 2 
for x in range(137, 160):
    print(f(x))
