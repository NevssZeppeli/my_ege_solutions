s = '1'*2019 + '3'*2119
while '11' in s:
    s = s.replace('11', '2', 1)
    s = s.replace('22', '3', 1)
    s = s.replace('33', '1', 1)
print(s)
