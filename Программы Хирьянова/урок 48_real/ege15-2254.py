A = 1
while not all((x%A == 0) <= ((x%28 != 0) or (x % 42 == 0))
              for x in range(10000)):
    A += 1
print(A)
