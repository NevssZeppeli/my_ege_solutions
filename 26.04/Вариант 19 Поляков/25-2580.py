gr = 0
lenn = 0
for x in range(586132, 586430+1):
    divs = [d for d in range(1, x+1) if x % d == 0]

    if len(divs) > lenn:
        lenn = len(divs)
        gr = x
    
print(gr)



#586430
