from itertools import permutations

word = 'ПЕСКАРЬ'
perms = [''.join(p) for p in permutations(word)]
count = 0
for x in perms:
    if x[1] != "Ь" and "ЬА" not in x and "ЬЕ" not in x and "ЬР" not in x:
        count+=1
print(count)
