f = open('1-5.txt')
line = f.readline()
counter = 0
m = []

for i in line:
    if line[i] == "Z":
        counter += 1
    if counter == 3:
        line[i]= ' Z'
    print(line)

print(m)