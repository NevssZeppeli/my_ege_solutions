x = 9 ** 8 + 3**25 - 14
print(x)
b = ' '
while x > 0:
    b = str(x%3)+b
    x = x//3
print(b)

one = b.count('1')
two = b.count('2')*2
print(one + two)