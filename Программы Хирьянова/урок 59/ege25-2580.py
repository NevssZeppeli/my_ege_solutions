def divs_number(x):
    n = 1
    for d in range(1, x//2+1):
        if x % d == 0:
            n += 1
    return n
    
the_numbers = []
max_divs_number = 0
for x in range(586132, 586430+1):
    dn = divs_number(x)
    if dn > max_divs_number:
        the_numbers = [x]
        max_divs_number = dn
    elif dn == max_divs_number:
        the_numbers += [x]
print(max_divs_number)
print(the_numbers[0], the_numbers[-1])
