with open('27-63b.txt') as file:
    file.readline()
    print(min(map(sum, combinations(sorted(map(int, file))[:50], 4))))
