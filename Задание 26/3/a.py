f = open('27881.txt') # Открываем файл

n = int(f.readline().split()[0]) # Свободное место на диске

data = sorted(map(int, f.readlines())) # Пользователи и их объем

total = 0 # Переменная для накопления объема

for i, val in enumerate(data):

	if total + val > n:

		break # Если объем выходит за границы, то прерываем цикл

	total += val # Накапливаем объем

print('Максимально число пользователей:', i)

delta = n - total # Оставшееся пространство на диске

candidates = [x for x in data if x - data[i-1] <= delta]

print('Максимальный объем пользователя:', max(candidates))