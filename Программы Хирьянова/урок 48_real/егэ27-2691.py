import sys
sys.stdin = open('27-31b.txt')
s_all = s_max = 0
min_delta = 10_000
N = int(input())
for i in range(N):
    a, b, c = (int(x) for x in input().split())
    s_all += a + b + c
    if b < c: b, c = c, b
    if a < b: a, b = b, a
    s_max += a
    for delta in (a - b, a - c):        
        if delta % 9 != 0 and delta < min_delta:
            min_delta = delta
if (s_all - s_max) % 9 == 0:
    s_max -= min_delta
print(s_all - s_max)
