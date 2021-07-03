def generate_succession(n: int):
    for i in range(n):
        print(f'in function, i={i}')
        yield i * 10

A = generate_succession(15)
for x in A:
    print('out of functoin', x)
