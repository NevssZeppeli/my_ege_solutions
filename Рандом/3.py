import sys
sys.setrecursionlimit(100000)

def f(n):
    if n <=5:
        return n
    elif n%8 == 0:
        return n + f((n/2)-3)
    else:
        return n + f(n+4)



print(f(6))