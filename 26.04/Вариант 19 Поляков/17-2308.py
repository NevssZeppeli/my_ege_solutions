b = []
for x in range(3394, 8600):
    if (x%3 ==1) and (x%7==5):
        print(x)
        b.append(x)
print(sum(b))
