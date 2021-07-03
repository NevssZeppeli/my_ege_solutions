for x in range(0, 100000):
    s = x
    #s = int(input())
    n = 0
    while 400 < s*s:
        s = s - 1
        n = n + 3
    #print(n)
    print(x, n)
    if n >= 1000:
        break
    
