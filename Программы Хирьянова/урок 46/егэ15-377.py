from functools import partial

def P(x):
    return 10 <= x <= 29

def Q(x):
    return 13 <= x <= 18

def checker(A: "some function from x"):
    diapasone = range(8, 32)
    return all(not A(x) or P(x) or Q(x) for x in diapasone)

def A(x, left, right):
    return left <= x <= right

max_len = 0
for left in range(8, 32):
    for right in range(left+1, 32):
        if (checker(partial(A, left=left, right=right)) and
           right - left > max_len):
            max_len = right - left
            l, r = left, right
print([l, r], "Ответ:", max_len)
