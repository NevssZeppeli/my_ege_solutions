# Лиса!
# Лиса!1
N = 7
A = list(range(1, N+1))
print(A)
# реверс списка самого в себе (поэлементно):
for i in range(N // 2):
    tmp = A[i]
    A[i] = A[N-1-i]
    A[N-1-i] = tmp
    print("DEBUG:", i, A)
print(A)
