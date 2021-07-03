n = int(input())
mods = [0] + [float('-inf')]*99

for _ in range(n):
    newmods = [float('-inf')]*100
    inp = int(input())
    for prev in mods:
        if type(prev) is not float:
            for x in 0, inp:
                res = x + prev
                newmods[res % 100] = max(newmods[res % 100], res)
        # print(newmods)
        mods = newmods[:]

print(mods[50])
