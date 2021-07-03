f = open('27.txt')
n = int(f.readline())
curr_sum = [0]*73
curr_len = [0]*73

msum = 0
mlen = 0

for i in range(n):
    x = int(f.readline())
    l = [0] * 73
    s = [0] * 73
    for i in range(73):
        if curr_sum[i]!=0:
            ost = (curr_sum[i] + x) % 73
            if curr_sum[i] + x > s[ost]:
                s[ost] = curr_sum[i] + x
                l[ost] = curr_len[i] + i
    if x > s[x%73]:
        s[x%73] = x
        l[x%73] = 1
    if s[0] > msum or s[0] == msum and l[0]<mlen:
        msum = s[0]
        mlen = l[0]
    curr_sum = s
    curr_len = l
print(mlen)