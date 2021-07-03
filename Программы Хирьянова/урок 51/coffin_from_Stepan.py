#Для чисел из отрезка [10^6, 10^36] найдите все такие числа, 
# у которых ровно 7 делителей,
# в ответ запишите их количество и наибольшее из них.
is_simple = [True]*10**6
for x in range(2, 10**3):
    if is_simple[x]:
        for y in range(x*x, 10**6, x):
            is_simple[y] = False
n = 0
last = None
for x in range(10, 10**6):
    if is_simple[x]:
        n += 1
        last = x
print(n, last**6)
