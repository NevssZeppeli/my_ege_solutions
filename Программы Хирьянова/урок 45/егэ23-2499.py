K = [0, 1, 1] + [None]*13
for n in range(3, 15 + 1):
    K[n] = K[n-1] + K[n-3] + (K[n // 3] if n % 3 == 0 else 0)
print(K[15])
