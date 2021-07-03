def formula(x, A):
    return ((x%A==0) <= ((x%A==0 <= x%34==0 and x%51==0)))
A = 1
while not all(formula(x,A) for x in range(1, 1000)):
    A+=1
print(A)
