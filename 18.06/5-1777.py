def f(n):
    n = bin(n)[2:]
    n+=n[-1]
    if n.count('1')%2 == 0:
        n+='0'
    else:
        n+='1'
    if n.count('1')%2 == 0:
        n+='0'
    else:
        n+='1'


    return int(n, 2)

for x in range(1, 100):
    if f(x) > 80:
        print(x)
        break