1a = int(input())
b = int(input())
# предположим, что a > b (а что, если наоборот???)
while b != 0:
    a, b = b, a % b
print(a)
