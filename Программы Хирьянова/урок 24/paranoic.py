def plus(a, b):
    if b == 0:
        return a
    else:
        return plus(a, b-1) + 1
    
def multiply(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return plus(multiply(a, b-1), a)

def power(a, b):
    if b == 0:
        return 1
    else:
        return multiply(power(a, b-1), a)
