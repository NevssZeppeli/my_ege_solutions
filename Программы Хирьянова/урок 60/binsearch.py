def upper_bound(A, key): 
    left = -1 
    right = len(A) 
    while right > left + 1: 
        middle = (left + right) // 2 
        if A[middle] > key: 
            right = middle 
        else:  # A[middle] <= key:
            left = middle
    assert right - left == 1, "Верю в то, что границы сомкнулись."
    return right

from random import randint
A = sorted(randint(1, 999) for i in range(20))
print(A)
x = int(input())
i = upper_bound(A, x) - 1
if i >= 0 and A[i] == x:
    print('нашёл')
