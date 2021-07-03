for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and not y) or (y == z) or w) == False:
                    print(x, y, z, w,
                          #int((x and not y) or (y == z) or w),
                          sep='\t')
