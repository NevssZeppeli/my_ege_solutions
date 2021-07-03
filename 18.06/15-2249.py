def form(x,A):
    return ((not(x%A==0))) <= ((not(x%24==0)) and (not(x%36 ==0)))

for A in range(1, 5000):
    if all(form(x,A) for x in range(1, 1000)):
        print(A)


'''
def delX(x,n):
    return x%n==0

def delA(x,A):
    return (((not(x%A==0))) <= ((not(x%24==0)) and (not(x%36 ==0))))

for A in range(1, 1000):
    f = True
    for x in range(1, 1000):
        if not delA(x,A):
            f = False
            break
    if f == True:
        print(A)
        '''