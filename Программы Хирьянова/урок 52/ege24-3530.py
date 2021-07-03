text = open('24-153.txt').read()
line = list(text)
n = 0
for width in range(7, 10 + 1):
    for i in range(len(line) - width + 1):
        if line[i] == "A" and line[i+width-1] == "F":
            n += 1
print(n)
