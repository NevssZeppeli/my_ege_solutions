x = 9**20 + 3**60 - 25
b = ''
while x > 0:
    b = str(x%3)+b
    x = x//3
print(b.count('2'))
    