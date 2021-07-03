# Требуется найти пару элементов с максимальной суммой
N = int(input("Сколько будет чисел?"))
M = 3  # расстояние не менее чем 3 между индексами элементов
Q = []
for i in range(M):
    x = int(input())
    Q.append(x)

max_left = -99999999
max_pair_sum = -999999999
for i in range(M, N):
    x = int(input())
    new_left = Q[0]
    if new_left > max_left:  # подновляю наилучшего левого
        max_left = new_left
    Q.pop(0)  # удалить левый элемент из очереди
    Q.append(x)  # добавить новый элемент в конец очереди

    if x + max_left > max_pair_sum:
        max_pair_sum = x + max_left
    
print(max_pair_sum)
1