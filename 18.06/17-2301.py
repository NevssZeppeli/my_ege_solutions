# Рассматривается множество целых чисел, принадлежащих отрезку [1305; 7850],
# которые делятся на 4 или на 7 и не делятся на 11, 17, 19 и 21.
# Найдите количество таких чисел и минимальное из них.
# В ответе запишите два числа через пробел: сначала количество, затем минимальное число.

s = []
count = 0
for x in range(1305, 7850+1):
    if ((x%4==0) or (x%7==0)) and ((x%11!=0) and (x%17!=0) and (x%19!=0) and (x%21!=0)):
        count+=1
        s.append(x)

print(count, min(s))