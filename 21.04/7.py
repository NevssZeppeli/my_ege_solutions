import itertools
w = 'ИЗУЧАТЙ'
k = itertools.permutations(w, 7)
n = 0
for x in list(k):
    word = ''.join(x)
    if word[1] != "Й":
        n+=1
print(n)
