from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 3, b), (a, b + 3), (a * 2, b), (a, b * 2) #действия зависят от задачи

@lru_cache(None) #мемоизация
def f(h):
    if sum(h) >= 78: #зависит от условия
        return 'W'
    if any(f(m) == 'W' for m in moves(h)):
        return 'P1'
    if any(f(m) == 'P1' for m in moves(h)): #девятнадцатое
       return 'B1P' #закомментировать обе строки по девятнадцатому, чтобы были решения для 20 и 21
    if all(f(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(f(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(f(m) == 'P1' or f(m) == 'P2' for m in moves(h)):
        return 'B2'
    

for s in range (1, 70+1):
    print(s, f( (7, s)) ) #кортеж по условию
