
def shift_left(A):
    """ циклический сдвиг влево (поэлементно) """
    tmp = A[0]
    for i in range(0, N-1):
        A[i] = A[i+1]  # В текущий кладу значение следующего.
        #print("DEBUG:", i, A)
    A[N-1] = tmp

def shift_right(A):
    """ циклический сдвиг вправо (поэлементно) """
    tmp = A[N-1]
    for i in range(N-2, -1, -1):
        A[i+1] = A[i]  # В следующий - значение текущего.
        print("DEBUG:", i, A)
    A[0] = tmp

N = 7
A = list(range(N))
print(A)
shift_right(A)
print(A)
