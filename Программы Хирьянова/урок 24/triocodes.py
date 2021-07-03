def combinations(n, prefix=""):
    "print all combinations of n bits with prefix"
    if n == 0:
        print(prefix)
    else:
        combinations(n-1, prefix + "0")
        combinations(n-1, prefix + "1")
        combinations(n-1, prefix + "2")

combinations(3)
