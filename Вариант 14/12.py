s = '563'*121

while (s.find('56', 1) or s.find('3333', 1)) != -1:
    s.replace('56', '3', 1)
    s.replace('3333', '3', 1)
print(s)