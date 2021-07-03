f = open('24.txt', 'r')
count =0
for x in f:
    if (f[x-1] == 'K' and f[x] == 'O' and f[x+1] == 'T'):
        count+=1
print(count)