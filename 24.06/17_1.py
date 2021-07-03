a = [x for x in range(1056, 7563+1) if (x%3==0 or x%11==0) and x%13!=0 and x%17!=0 and x%19!=0 and x%23!=0]
print(len(a), min(a))