s = '2'*103

while '222' in s:
    s = s.replace('22', '7', 1)
    s = s.replace('77', '2', 1)
print(s)