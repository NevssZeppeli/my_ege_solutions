count = 0
for x in range(2568, 7858):
    if (x%5==0 or x%4==0) and x%11!=0 and x%20!=0 and x%27!=0:
        count+=1
        print(x)

print('кол-во:', count)