import sys
sys.stdin = open('26-14.txt')

S = int(input())
N = int(input())

count = 0
numbers =[]

for x in range(N):
    x = int(input())
    numbers.append(x)


for i in range(0, N):
    for j in range(i+1, N):
        if numbers[i]+numbers[j] <= S:
            print(numbers[i], numbers[j])
