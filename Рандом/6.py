'''
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (x and y) or (not x and not z) == True:
                print(x,y,z)
'''

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and not y) or (y == z) or w) == False:
                    print(x,y,z,w)

