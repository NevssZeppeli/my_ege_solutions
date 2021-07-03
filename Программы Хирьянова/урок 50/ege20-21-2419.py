win_rate = [[-1]*(62*2) for i in range(62*2)]
turns_to_end = [[0]*(62*2) for i in range(62*2)]
for y in range(60, 0, -1):
    # [x+y<62] => [x<62-y] => [x<=61-y]
    for x in range(61 - y, 0, -1):
        moves = [(x+3, y), (x, y+3), (x*2, y), (x, y*2)]
        win_rate[x][y] = -min(win_rate[a][b] for a, b in moves)
        turns_to_end[x][y] = 1 + (min if win_rate[x][y] == 1 else max)(
            turns_to_end[a][b] for a, b in moves
            if win_rate[a][b] != win_rate[x][y])

for s in range(1, 61):
    if turns_to_end[7][s] == 3:
        print("Петя выигрывает 2-м ходом (всего 3 хода):", s)
for s in range(1, 61):
    if turns_to_end[7][s] == 4:
        print("Ваня выигрывает 2-м ходом (всего 4 хода):", s)
                
        
