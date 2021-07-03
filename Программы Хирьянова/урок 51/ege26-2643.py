import sys
sys.stdin = open('26-j1.txt')
c = [0]*100
N = int(input())
for i in range(N):
    x = int(input())
    c[x] += 1
k = 0
for x in range(1, 50):  # не включаю корзины по 50 монет!
    k += min(c[x], c[100-x])
k += c[50] // 2
print(k)
