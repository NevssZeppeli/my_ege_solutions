n = 0
for a in 'КУМА':
    for b in 'КУМА':
        for c in 'КУМА':
            for d in 'КУМА':
                word = a+b+c+d
                if a and b in("У", "А"):
                    n+=1
                    print(word)
                    print(n)
