def gameover(pos):
    return pos[0] + pos[1] >= 62

def moves(pos):
    x, y = pos
    return [(x + 3, y),
            (x, y + 3),
            (2*x, y),
            (x, 2*y)]
for s in range(1, 54):
    pos0 = (7, s)
    pos1_p = moves(pos0)
    if any(gameover(pos) for pos in pos1_p):
        # у Пети есть взоможнось выиграть 1-м ходом
        continue
    sum_flag = True  # нужно, чтобы для любого из pos1_p удавалось выиграть Ване3
    for pos_v in pos1_p:
        pos1_v = moves(pos_v) #pos1_v - позиции для 2-го хода Пети (после Вани)
        flag = False
        for pos_p in pos1_v:
            pos2_p = moves(pos_p)
            if any(gameover(pos) for pos in pos2_p):
                # у Пети есть взоможнось выиграть 2-м ходом
                continue
            # pos2_p - позиции для 2-го хода Вани
            if all(max(x, y)*2 + min(x, y) >= 62 for x, y in pos2_p):
                flag = True
        if not flag: # если у Вани нет хода, который даст ему возможность выиграть
            sum_flag = False
    if sum_flag:
        print(pos0, "подходит")
