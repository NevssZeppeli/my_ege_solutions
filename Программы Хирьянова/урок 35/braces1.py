sequence = input()
is_correct = True
Q = []
for brace in sequence:
    print('DEBUG', *Q, ' + ', brace)
    if brace == '(' or brace == '[':
        Q.append(brace)
    elif brace == ')' or brace == ']':
        if len(Q) == 0:  # А левых открытых-то нет!!!
            is_correct = False
            break  # дальше можно не смотреть
        left = Q.pop()
        if (brace == ')' and left !='(' or
            brace == ']' and left !='['):
            is_correct = False
            break  # дальше можно не смотреть
                
if len(Q) > 0:  # остались левые не закрывшиеся
    is_correct = False
print("Скобочное выражение",
      "корректно" if is_correct else "некорректно")
