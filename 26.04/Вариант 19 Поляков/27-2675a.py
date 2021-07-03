import sys
sys.stdin = open('27-15a.txt')

numbers = []

N = int(input())
for x in range(1, N+1):
    x = int(input())
    numbers.append(x)
#print(numbers)

count = 0
for i in range(0, N-5):
    for j in range(i+5, N):
        if ((numbers[i] + numbers[j]) % 14 == 0):
            print(numbers[i], numbers[j])
            count +=1
print("кол-во: ", count)
