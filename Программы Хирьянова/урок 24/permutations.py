def permutations(n: "int,<10", prefix=""):
    "print all permutations of n digits"
    if len(prefix) == n:
        print(prefix)
    else:
        for x in range(n):
            if str(x) not in prefix:
                permutations(n, prefix + str(x))

permutations(5)
