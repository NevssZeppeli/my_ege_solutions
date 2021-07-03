def form(x, A):
    # ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 9))
    return ((not(x%A==0)) <= ((x%6==0) <= (not (x%9==0))))
for A in range(1, 1000):
    if all(form(x,A) for x in range(1, 1000)):
        print(A)