import random

def merge(A,B):
    '''возвращает C'''
    C = [None]*(len(A) + len(B))
    i = 0
    k = 0
    n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merge_sorted(A):
    """ Возвращает *новый* список из элементов А,
        но отсортированный по возрастанию.
        А остаётся нетронутым
    """
    if len(A) <= 1:
        return list(A)  # новый список на основании А
    middle = len(A) // 2
    left = A[:middle]  # первая половина списка
    right = A[middle:]  # вторая половина списка
    return merge(merge_sorted(left), merge_sorted(right))


N = int(input("Введите размер списка для теста сортировки: "))
A = [random.randint(0, 999) for i in range(N)]
B = merge_sorted(A)
#print(*A, sep='\t')
#print(*B, sep='\t')

