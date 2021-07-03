def left_barrier(A: "sorted list of numbers", y: "num to find"):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < y:
            left = middle
        else:  # A[middle] >= y  ==> это "поджималка" левой границы
            right = middle
    return left

def right_barrier(A: "sorted list of numbers", y: "num to find"):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= y:
            left = middle  # left - это "поджималка" левой границы
        else:  # A[middle] > y
            right = middle
    return right

def find_element(A: "sorted list of numbers", y: "num to find"):
    left = left_barrier(A, y)
    right = right_barrier(A, y)
    if right - left == 1:
        print("Такого числа нет в массиве.")
    else:
        print("в массиве это число встречается", right - left - 1, "раз")
        print("расположено с индекса", left + 1)
        print("до индекса", right - 1)

from random import *
A = [randint(0, 9) for i in range(40)]
A.sort()
print(A)
y = int(input())
find_element(A, y)




