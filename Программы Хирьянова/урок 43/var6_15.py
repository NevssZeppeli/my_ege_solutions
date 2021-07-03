def formula(x, A):
    return (not ((x % A == 0) and (x % 21 == 0)) or
     (x % 18 == 0))

A = 1
while not all(formula(x, A) for x in range(1, 1000)):
    A += 1
print(A)
