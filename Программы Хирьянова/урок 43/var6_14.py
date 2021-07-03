x = 9**7 + 3**21 - 8
s = 0
while x != 0:
    s += x % 3
    x //= 3
print(s)
