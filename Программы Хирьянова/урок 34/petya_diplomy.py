
w, h, n = [int(word) for word in input().split()]
f = lambda a: (a // w)*(a // h) # число дипломов на квадрате со стороной a
left = 0
right = min(w, h) * n
while right - left > 1:  # до двух соседних значений
    middle = (left + right) // 2
    if f(middle) < n:
        left = middle  # f(left) < требуемого числа дипломов
    else:
        right = middle  # f(right) >= нужного числа     
print(right)
        
    
