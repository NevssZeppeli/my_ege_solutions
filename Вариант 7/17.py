count = 0
for x in range(5883, 15906):
    if ((x%9 == 0) or (x%23==0)) and ((x%13!=0) and (x%18!=0) and (x%19!=0) and (x%22!=0)):
        count+=1
        print(x)
        print(count)
