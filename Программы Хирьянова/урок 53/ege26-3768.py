file = open("26-52.txt")
N = int(file.readline())
data = sorted(map(int, file.readlines()))
delta = 100 + 1
count = 0
min_sum = 2*10**9
for i in range(0, N - 1):
    for k in range(i+1, min(i + delta + 1, len(data))):
        s = data[i] + data[k]
        if s % 10 == 0:
            count += 1
            if s < min_sum:
                min_sum = s
print(count, min_sum/2)
