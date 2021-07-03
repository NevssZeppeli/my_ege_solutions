# Все возможные делители числа (примитивно)
x = int(input())
all_divisors = [d for d in range(1, x+1) if x % 2 == 0]
print(all_divisors)







