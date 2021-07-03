a = [x for x in range(2477,7850) if x%2==0 and x%5!=0 and x%8!=0 and x%9!=0 and x%13!=0]
print(len(a), min(a))