maximum = 0
count = 0
for x in range(3201, 12877):
    if (x % 4 == 0) and (x%7!=0) and (x%11!=0) and (x%13!=0) and (x%19!=0):
        count += 1
        if x > maximum:
            maximum = x
print(count, maximum)