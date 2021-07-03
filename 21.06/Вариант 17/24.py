f = open('24-5.txt')
count = 0
c = 0
s = f.read()
for x in range(len(s)):
    c+=1
    if s[x] == ")":
        count+=1
        if count==10000:
            print(c)


