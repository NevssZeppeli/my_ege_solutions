с = 0
for x in 'НОДА':
    for y in 'НОДА':
        if x == y: continue
        for w in 'НОДА':
            if w in x + y: continue
            for z in 'НОДА':
                if z in x + y + w: continue
                
                word = x+y+z+w
                if ('ОА' not in word) and ('АО' not in word) and ('НД' not in word) and ('ДН' not in word):
                        print(word)
