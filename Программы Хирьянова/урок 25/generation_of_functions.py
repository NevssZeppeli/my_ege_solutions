from random import randint

def generator_of_functions1():
    def f0(x): return x
    def f1(x): return x * 2
    def f2(x): return x + 3
    rnd_number = randint(0, 2)
    if rnd_number == 0:
        return f0
    elif rnd_number == 1:
        return f1
    elif rnd_number == 2:
        return f2

def generator_of_functions2():
    def f0(x): return x - 1
    def f1(x): return x * 5
    def f2(x): return x + 7
    list_of_functions = [f0, f1, f2]
    return list_of_functions[randint(0, 2)]

def generator_of_functions3():
    list_of_functions = [lambda x: x - 1,
                         lambda x: x * 5,
                         lambda x: x + 7]
    return list_of_functions[randint(0, 2)]




n = int(input("Выберите генератор функций (1 или 2):"))
generator = [generator_of_functions1, generator_of_functions2][n-1]

f = generator()
for x in range(0, 10):
    print(f(x), end='\t')
    
