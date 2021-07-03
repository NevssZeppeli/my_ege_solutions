def form(x,A):
    return (((x%40==0) or (x%64==0)) <= (x%A==0))

a = []
for A in range(1, 10000):
    if all(form(x,A) for x in range(1, 10000)):
        a.append(A)

print(max(a))