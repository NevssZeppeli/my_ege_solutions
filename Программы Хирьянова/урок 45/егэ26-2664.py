file = open('26-j2.txt')
N = int(file.readline())
A = []
for i in range(N):
    x = file.readline()
    A.append(int(x))
A.sort()
median = A[N//2]
mean = sum(A) / N
num_of_numbers = sum((mean <= x <= median) for x in A)    
print(num_of_numbers)
