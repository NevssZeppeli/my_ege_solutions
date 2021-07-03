import sys
sys.stdin = open('27-27b.txt')
s_max = 0
d_min = 10000
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    s_max += max(x, y)
    if (x - y) % 16 != 0:
        d_min = min(d_min, abs(x - y))
if s_max % 16 == 0xA:
    s_max -= d_min
print(s_max)
