
for x in range(174457, 174505 + 1):
    divs = [d for d in range(2, x) if x % d == 0]
    if len(divs) == 2:
        print(*divs)

            
