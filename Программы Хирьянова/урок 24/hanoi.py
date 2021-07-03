def hanoi_solver(n, start, finish):
    assert start != finish, "Нельзя перекладывать на тот же столбец"
    assert start in (1, 2, 3) and finish in (1, 2, 3), \
           "допустимо только 1, 2, 3"
    assert n >= 1, "Можно перекладывать пирамиду только положительной высоты"

    if n == 1:
        print(f"Переложить блин 1 с {start} на {finish}.")
    else:
        tmp = 6 - start - finish
        hanoi_solver(n - 1, start, tmp)
        print(f"Переложить блин {n} c {start} на {finish}.")
        hanoi_solver(n - 1, tmp, finish)

hanoi_solver(5, 1, 2)
