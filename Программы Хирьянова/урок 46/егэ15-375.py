#(X & 49 ≠ 0) → ((X & 33 = 0) → (X & A ≠ 0))
universum = range(0, 64)
A = 1
while (not all((x & 49 == 0) or (x & 33 != 0) or (x & A != 0)
               for x in universum)):
    A += 1
print(A)
