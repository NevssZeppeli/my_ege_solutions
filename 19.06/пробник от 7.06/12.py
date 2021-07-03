x = '9'*100 + "1"*14 + '2'*48

while '999' or '22' in x:
    if '999' in x:
        x = x.replace('999', '12')
    else:
        x = x.replace('22', '1')

print(x)