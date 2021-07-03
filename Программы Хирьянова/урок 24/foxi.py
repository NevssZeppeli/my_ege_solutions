name = "ФОКСИ"
def foksi(n: "int,<10", prefix: list):
    "print all permutations of n numbers"
    if len(prefix) == n:
        print(*(name[i] for i in prefix))
    else:
        for x in range(n):
            if x not in prefix:
                foksi(n, prefix + [x])

foksi(5, [])
