import sys
sys.stdin = open('27-20b.txt')
N = int(input())
last_bone = [int(x) for x in input().split()]
L = [[1, 1] for i in range(N+1)]
for k in range(2, N+1):
    bone = [int(x) for x in input().split()]
    for p in range(2):
        for q in range(2):
            if bone[p] == last_bone[1-q]:
                L[k][p] = L[k-1][q] + 1
    last_bone = bone
print(max(max(n1, n2) for n1, n2 in L))

print(max(max(L, key=max)))
