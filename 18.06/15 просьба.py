def form(x,A):
    return (((x%A==0) and (x%24==0) and (not (x%16==0))) <= (not (x%A==0)))

for A in range(1, 5000):
    if all(form(x,A) for x in range(1, 1000)):
        print(A)