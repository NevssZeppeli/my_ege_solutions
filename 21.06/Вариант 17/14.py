x = 9**8 + 3**24 - 6
b = ''
while x>0:
    b = str(x%3)+b
    x//=3
print(b.count('2'))