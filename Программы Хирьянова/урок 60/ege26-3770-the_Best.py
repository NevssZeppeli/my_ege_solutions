file = open("26-53.txt")
N = int(file.readline())
numbers = set(int(file.readline()) for i in range(N))
evens = [x for x in numbers if x % 2 == 0]
mean_values = []
for i in range(len(evens)):
    for k in range(i + 1, len(evens)):
        mean = (evens[i] + evens[k]) // 2
        if mean in numbers:
            mean_values.append(mean)
print(len(mean_values), min(mean_values))
