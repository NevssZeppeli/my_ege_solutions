def F(x, y, A):
    return (36 != y + 2*x) or (8*x > A) or (2*y > A)

Z = range(0, 100)
for A in range(0, 1000):
    if all(F(x, y, A) for x in Z for y in Z):
        print(A)
