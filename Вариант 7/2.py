for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not(x == (not z)) or ((x or w) == y) == False:
                    print(w, x, y, z) 