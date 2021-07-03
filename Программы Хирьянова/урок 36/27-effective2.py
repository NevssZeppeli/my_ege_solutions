# Задача https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=2673
import time
import sys
sys.stdin = open('27-13b.txt')

t1 = time.process_time_ns()

N = int(input())
pairs_number = k2 = k7 = k14 = 0
Q = [int(input()) for i in range(7)]
current = 0
for j in range(7, N):
    y = int(input())
    x = Q[current]  # циклическая очередь фиксированной длины
    Q[current] = y
    current = (current + 1) % 7  # отслеживание очередного в очереди
    if x % 14 == 0:
        k14 += 1
    if x % 7 == 0:
        k7 += 1
    if x % 2 == 0:
        k2 += 1
    if y % 14 == 0:
        pairs_number += j - 7 + 1  # все допустимые левые подходят
    elif y % 7 == 0:  # автоматически y не может ТАКЖЕ делиться на 2
        pairs_number += k2  # число делящихся на 2 допустимых левых
    elif y % 2 == 0:  # автоматически y не может ТАКЖЕ делиться на 7
        pairs_number += k7  # число делящихся на 7 допустимых левых
    else:  # автоматом не делится ни на 2, ни на 7.
        pairs_number += k14  # число делящихся на 14 допустимых левых
print(pairs_number)

t2 = time.process_time_ns()
print(t2 - t1, "nanoseconds")
