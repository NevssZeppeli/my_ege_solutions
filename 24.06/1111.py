s = '1'*81

while '1111' in s or '8888' in s:
    if '1111' in s:
        s = s.replace('1111', '888', 1)
    else:
        s = s.replace('8888', '8', 1)
print(s)
