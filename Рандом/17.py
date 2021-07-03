n = 0
for x in range(1216, 8824+1):
    if ((x % 3 ==0) and (x % 7 != 0) and (x % 15 != 0) and (x % 17 != 0 )and (x % 21 != 0)):
           n +=1
           print(x)
print(n)           
