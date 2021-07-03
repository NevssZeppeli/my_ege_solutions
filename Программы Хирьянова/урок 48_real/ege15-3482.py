def F(x, y, A):
    return ((y - 40 < A) and (30 - y < A)) or (x * y > 20)

for A in range(1, 100):
    """all_ = True
    for x in range(100):
        for y in range(100):
            all_ = all_ and F(x, y, A)
    """
    print(A, all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)))
    
