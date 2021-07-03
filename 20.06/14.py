x = 4**625 - 2**311 + 2**571 - 48

b = ''
while x > 0:
    b = str(x%4)+b
    x//=4
print(b.count('1'))
