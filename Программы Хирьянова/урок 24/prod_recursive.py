def production(n: int):
    if n == 0:
        return 1
    else:
        return int(input()) * production(n - 1)

