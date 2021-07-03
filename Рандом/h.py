n = 0
for a in "АБВГДЕ":
    for b in "АБВГДЕ":
        for c in "АБВГДЕ":
            for d in "АБВГДЕ":
                for e in "АБВГДЕ":
                    word = a+b+c+d+e
                    if (word.count("А") == 1 and word.count("Б") == 1):
                        n += 1
                        print(word)
print(n)
