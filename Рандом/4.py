count = 0
for x in range(-999, 999+1):

    y = hex(x)
    str(y)
    if y[-1] == "f" and x % 12 != 0 and x % 13 != 0:
        print(x)
        count += 1

print(count)

