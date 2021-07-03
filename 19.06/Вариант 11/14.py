x = 9**14 + 3**18 - 9**5 - 27
b = ''
while x>0:
    b = str(x%3) + b
    x//=3

print(b.count('2'))