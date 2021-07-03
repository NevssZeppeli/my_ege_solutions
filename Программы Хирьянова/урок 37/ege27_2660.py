import sys
sys.stdin = open("27-b.txt")

def gen(n: int, pairs: list, prefix: list):
    if n == len(pairs):
        s = sum(prefix)
        return s if (s % 3 != 0) else 01
    else:
        result1 = gen(n+1, pairs, prefix + [pairs[n][0]])
        result2 = gen(n+1, pairs, prefix + [pairs[n][1]])
        return max(result1, result2)

N = int(input())
pairs = []
for i in range(N):
    x, y = (int(word) for word in input().split())
    pairs.append((x, y))
print(gen(0, pairs, []))
