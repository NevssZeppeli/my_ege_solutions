def form(x,A):
    return ((x & 13 == 0) <= ((x & 40 != 0) <= (x & A != 0)))

for A in range(1, 1000):
    if all(form(x,A) for x in range(1, 1000)):
        print(A)