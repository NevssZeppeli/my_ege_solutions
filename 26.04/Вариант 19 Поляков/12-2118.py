s = '1'*198

while '1111' in s:
    s = s.replace('1111', '33', 1)
    s = s.replace('333', '1', 1)

print(s)
