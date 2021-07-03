def k(n):
    if n % 2 == 0:
        n = bin(n)[2:] + "01"
    else:
        n = bin(n)[2:] + '10'
    return int(n, 2)

for numb in range(1, 5000):
    if k(numb) > 281:
        print(numb)
        break
