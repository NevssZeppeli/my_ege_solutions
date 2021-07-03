import time
t1 = time.time()
# -------------------------
import sys
sys.stdin = open('27-13b.txt')

N = int(input())
a = [int(input()) for i in range(N)]
pairs_number = 0
for j in range(1, N):
    for i in range(0, j):
        if i + 7 <= j and a[i]*a[j] % 14 == 0:
            pairs_number += 1
print(pairs_number)
# ------------------------------
t2 = time.time()
print(t2 - t1, 'seconds')
