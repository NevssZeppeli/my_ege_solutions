def delX(x,n):
    return x%n==0

def delA(x,A):
    return ((delX(x,A) and (not delX(x,16))) <= delX(x,23))

for A in range(1, 1000):
    f = True
    for x in range(1, 1000):
        if not delA(x,A):
            f = False
            break
    if f == True:
        print(A)