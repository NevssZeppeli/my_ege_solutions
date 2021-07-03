from itertools import combinations_with_replacement
count = 1
a = set(combinations_with_replacement('AB123',8))
for x in a:
    if x.count("A") == 1 and x.count("B") == 1:
        count+=1
        print(x)
print(count)