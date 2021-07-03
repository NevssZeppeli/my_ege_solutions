from statistics import mean # Импортируем модуль для расчета среднего

f = open('26.txt') # Открываем файл

info = f.readline().split() # Считываем информацию n, k, m и делаем из нее список

prices = sorted(map(int, f.readlines())) # Записываем цены и сортируем

lowcost = prices[:int(info[1])] # Цены бюджетных смартфонов

highcost = prices[-int(info[2]):] # Цены смартфонов премиум сегмента

print('Самый дешевый смартфон премиум сегмента:', highcost[0]) 
print('Средняя цена бюджетного смартфона:', int(mean(lowcost) // 1))