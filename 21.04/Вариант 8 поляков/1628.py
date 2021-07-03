for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and z) or ((w <= x) == (z <= y))) == False:
                    print(x,y,z,w)
