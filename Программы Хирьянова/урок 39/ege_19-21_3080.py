s_end = 38
w = [None]*s_end + [-1]*s_end
for s in range(s_end-1, 0, -1):
    w[s] = -min(w[s+1], w[s+2], w[s+3], w[s*2])

n = [None]*s_end + [0]*s_end
for s in range(s_end-1, 0, -1):
    if w[s] == +1: # для выигрышной - хотим быстрее выиграть
        n_min = 99999999
        for k in s+1, s+2, s+3, s*2:
            if w[k] == -1 and n[k] < n_min:
                n_min = n[k]
        n[s] = n_min + 1
    else:  # для проигрышной - пытаемся затянуть игру
        n[s] = max(n[s+1], n[s+2], n[s+3], n[s*2])
print(*range(s_end), sep='\t')
print(*w[:s_end], sep='\t')
print(*n[:s_end], sep='\t')

