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

file = open("26-53.txt")
N = int(file.readline())
numbers = sorted(int(file.readline()) for i in range(N))
evens = [x for x in numbers if x % 2 == 0]
mean_values = []
for i in range(len(evens)):
    for k in range(i + 1, len(evens)):
        mean = (evens[i] + evens[k]) // 2
        m = upper_bound(numbers, mean) - 1
        if m >= 0 and numbers[m] == mean:
            mean_values.append(mean)
print(len(mean_values), min(mean_values))

