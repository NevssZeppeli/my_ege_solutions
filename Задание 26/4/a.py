f = open('27882.txt') # Открываем файл

n = int(f.readline().split()[0]) # Считываем объем диска

data = sorted(map(int, f.readlines())) # Записываем объем пользователей и сортируем

total = 0

for i, val in enumerate(data):

	if total + val > n:

		break

	total += val

print('Максимальное число пользователей:', i)

delta = n - total

maxvol = [x for x in data if x - data[i-1] <= delta]

print('Максимальный объем файла:', maxvol[-1])