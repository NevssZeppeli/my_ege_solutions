a = [x for x in range(14014, 49635 + 1) if x % 13 == 5 and x % 5 != 0 and x % 11 != 0]
print(len(a), max(a))
