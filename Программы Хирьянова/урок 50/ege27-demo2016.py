import sys; sys.stdin = open("Zadanie_27-B-demo2016.txt")
N = int(input())
queue_length = 6
Q = [int(input()) for i in range(queue_length)]
m = 1001  # минимальное среди всех, прошедших очередь (условная infinity)
m2 = 1001  # минимальное среди чётных, прошедших очередь (условная infinity)
min_prod = 1001*1001  # условная infinity^2
for i in range(queue_length, N):
    # вытащить из очереди число и подновить оптимальные парные:
    y = Q[i % queue_length]
    m = min(m, y)  # минимальное любое
    if y % 2 == 0:  # минимальное чётное
        m2 = min(m2, y)
    # подновляем минимальное произведение, с учётом того, чтобы оно было чётным
    x = int(input())
    if x % 2 == 0 and m != 1001:
        min_prod = min(min_prod, x * m)
    elif x % 2 == 1 and m2 != 1001:
        min_prod = min(min_prod, x * m2)
    Q[i % queue_length] = x
print(-1 if min_prod == 1001 * 1001 else min_prod)
