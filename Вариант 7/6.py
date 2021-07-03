count = 0
for x in range(5913, 11753):
  if (x%5 == 0) and (x%11 == 0) and not (x%7 == 0) and not (x%10 == 0) and not (x%13 == 0) and not (x%22 == 0):
    count+=1
    print(x)
print(count) 
