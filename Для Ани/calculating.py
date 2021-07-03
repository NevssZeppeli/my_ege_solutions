# Задача №112151. Случайные целые

from random import randint

a, b = input().split()


def calc(a, b):
    x = [randint(a, b) for i in range(5)]
    return x
print(*calc(int(a), int(b)))