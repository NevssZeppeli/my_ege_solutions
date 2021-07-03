#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=2353
lines = """
6	69	3	76	69	42	61	85	36	65
1	57	2	19	58	59	56	1	37	97
25	55	56	71	59	54	94	94	52	24
86	86	7	30	5	2	94	13	89	3
56	15	78	32	56	51	34	79	5	6
52	16	41	96	87	3	53	98	18	100
32	80	78	66	34	83	13	93	29	64
92	82	34	41	43	97	13	99	40	72
10	46	73	56	59	20	43	32	58	1
61	37	99	76	73	69	3	10	93	68
""".strip().splitlines()
coins = [ [int(word) for word in line.split()] for line in lines]
N = len(coins)
min_coins = [[0]*N for i in range(N)]
max_coins = [[0]*N for i in range(N)]
min_coins[0][0] = max_coins[0][0] = coins[0][0]
for i in range(1, N):
    min_coins[0][i] = min_coins[0][i-1] + coins[0][i]
    max_coins[0][i] = max_coins[0][i-1] + coins[0][i]
    min_coins[i][0] = min_coins[i-1][0] + coins[i][0]
    max_coins[i][0] = max_coins[i-1][0] + coins[i][0]
for i in range(1, N):
    for k in range(1, N):
        max_coins[i][k] = (max(max_coins[i-1][k], max_coins[i][k-1])
                           + coins[i][k])
        min_coins[i][k] = (min(min_coins[i-1][k], min_coins[i][k-1])
                           + coins[i][k])
print(max_coins[9][9], min_coins[9][9])    

