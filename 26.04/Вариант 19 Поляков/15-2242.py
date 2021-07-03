def formula(x,A):
    return (((not(x%A==0)) and (not(x%6==0))) <= (not(x%3==0)))
A=2 #потому что там есть деление x на A, а это даёт вариант 1
while not all(formula(x,A) for x in range(1, 10000)):
    A+=1
    print(A)

