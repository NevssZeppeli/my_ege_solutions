for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                #f = ((not x or z) and (not z or w)) or (y ==(x or z))
                f = (x <= z) and (z <= w) or (y == (x or z))
                if f == 0:
                    print(x, y, z, w)
