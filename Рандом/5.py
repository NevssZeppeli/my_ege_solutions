count = 0
for x in range(-5000, 5000+1):
    y = hex(x)
    if y[-1] == 'b' and x%6 != 0 and x%5 ==0 and x%7==0:
        count+=1
        print(x, count)