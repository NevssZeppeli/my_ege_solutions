for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((x<=z) and (z <= w)) or y == (z or x)) == False:
                    print(x,y,w,z)
