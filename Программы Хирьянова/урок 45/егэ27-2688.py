
import sys
sys.stdin = open('27-28b.txt')
s = 0
min_distance = 9999999
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    s += min(x, y)
    distance = abs(x - y)
    if distance % 8 != 0 and distance < min_distance:
        min_distance = distance
if s % 8 == 2:  # восьмеричная запись заканчивается на 2
    s += min_distance
print(s)
