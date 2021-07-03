file = open('24-s1.txt')
counter = 0
for line in file:
    if line.count('J') > line.count('E'):
        counter += 1
print(counter)
