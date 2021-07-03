a=[]
for i in range(174457,175505+1):
    b=[]
    sqri=int(i**0.5)
    for j in range(1, sqri+1):
        if i%j==0:
            a.append(j)
            a.append(i//j)
        if len(b)>4:
            break
    if len(b)==4:
        a.append(b)
print(a, '/n')