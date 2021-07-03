function_text = input("введите функцию от x: ")
f = lambda x: eval(function_text)
a, b = [float(word) for word in
        input("Промежуток для поиска корня (два числа через пробел): ").split()]
error = float(input("С какой погрешностью ищем корень: "))
if f(a)*f(b) >= 0:
    print("На этом промежутке нельзя воспользоваться двоичным поиском.")
    exit(0)
while (b - a) / 2 > error:
    c = (a + b) / 2
    if f(c) == 0:
        break  # наткнулись на корень ровно посередине. Что с погрешностью?..
    elif f(a)*f(c) < 0:
        b = c
    else:  # f(a) * f(c) > 0
        a = c
print("Корень f(x) = 0:", (a + b) / 2, "+-", (b - a) / 2)
        
    
