a = [x for x in range(34516, 95433+1) if (x%10 == 5 or x%10 == 3) and x%7 != 0 and x%11 != 0]
print(len(a), min(a))