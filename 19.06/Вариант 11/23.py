def f(curr, end):
    if curr > end:
        return 0
    if end == curr:
        return 1
    if curr < end:
        return f(curr+3, end) + f(curr*2, end) + f(curr*3, end)

print(f(1,18))