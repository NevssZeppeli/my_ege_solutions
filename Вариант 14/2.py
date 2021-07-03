for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((z or y) <= (x==z)) == False:
                print(x,y,z)