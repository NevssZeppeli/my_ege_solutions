N, *A = map(int, open('27-62b.txt').readlines())
A.sort()
#print(A, sep='\t')
max_progression_length = 1
for step in range(1, 100 + 1):
    L = [1]*N
    for i in range(1, N):
        k = i - 1
        while k > 0 and A[i] - A[k] < step:
            k -= 1
        if A[i] - A[k] == step:  # НАШЛИ предыдущий член прогрессии для A[i]
            L[i] = L[k] + 1  # А значит прогрессия удлиняется
            #Заодно ищем максимальную длину
            if L[i] > max_progression_length:
                max_progression_length = L[i]
                max_progression_step = step
                max_progression_last_element = A[i]
    #print(L, step, sep='\t')  # DEBUG
print(max_progression_length)
max_progression_first_element = (
    max_progression_last_element
    - max_progression_step * (max_progression_length-1))
progression = range(max_progression_first_element,
                    max_progression_last_element+1,
                    max_progression_step)
print('\t'.join(map(str, progression)))
