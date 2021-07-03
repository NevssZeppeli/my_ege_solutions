N = int(input())
s_min = 0
n_odd = 0
from_even_to_odd_min_distance, from_even_to_odd_min_distance2 = 10001, 10001
from_odd_to_even_min_distance, from_odd_to_even_min_distance2 = 10001, 10001
for i in range(N):
    x, y = (int(w) for w in input().split())
    s_min += min(x, y)
    n_odd += min(x, y) % 2  # +1, если x - нечётное число
    if abs(x - y) % 2 == 1:  # Если x, y имеют разную чётность
        if min(x, y) % 2 == 1: # меньшее - нечётно
            distance = max(x, y) - min(x, y)
            if distance < from_odd_to_even_min_distance:
                from_odd_to_even_min_distance2 = from_odd_to_even_min_distance
                from_odd_to_even_min_distance = distance
            elif distance < from_odd_to_even_min_distance2:
                from_odd_to_even_min_distance2 = distance1
        else:  # меньшее из двух - чётно
            distance = max(x, y) - min(x, y)
            if distance < from_even_to_odd_min_distance:
                from_even_to_odd_min_distance2 = from_even_to_odd_min_distance
                from_even_to_odd_min_distance = distance
            elif distance < from_even_to_odd_min_distance2:
                from_even_to_odd_min_distance2 = distance
print(s_min, n_odd)
print(from_even_to_odd_min_distance, from_even_to_odd_min_distance2)
print(from_odd_to_even_min_distance, from_odd_to_even_min_distance2)
# Большой ФИКСМИ
