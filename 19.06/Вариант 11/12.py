s = '1' * 110
while '111' in s:
    s = s.replace('111', '2')
    s = s.replace('222', '3')
    s = s.replace('333', '1')

print(s)