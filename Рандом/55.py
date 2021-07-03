def f(x: int):
    y = bin(x)[2::]
    if str(y).count('1') % 2 == 0:
        y += '0'
    else:
        y += '1'
    if str(y).count('1') % 2 == 0:
        y += '0'
    else:
        y += '1'   
    print(y)
    
for x in range(10, 38+1):
    f(x)
