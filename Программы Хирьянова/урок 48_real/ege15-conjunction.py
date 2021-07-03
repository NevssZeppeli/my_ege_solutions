def F(x, A):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))

A = 1
while not all(F(x, A) for x in range(1, 1000)):
    A += 1
print(A)
    
