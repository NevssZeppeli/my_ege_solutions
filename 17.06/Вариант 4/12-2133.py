x = '1'*2019 + '2'*2050

while '222' in x:
    x = x.replace('222', '1', 1)
    x = x.replace('111', '2', 1)
print(x)