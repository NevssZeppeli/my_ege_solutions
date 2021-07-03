n = 0
for a in "МАГИСТР":
    for b in "МАГИСТР":
        if b == a: continue
        for c in "МАГИСТР":
            if c == a or c == b: continue
            for d in "МАГИСТР":
                if d in a + b + c: continue
                for e in "МАГИСТР":
                    if e in a + b + c + d: continue
                    word = a + b + c + d + e
                    if "А" in word and "И" in word: continue
                    n += 1
print(n)
