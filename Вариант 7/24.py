f = open("24.txt", "r")
curlen = 1
maxlen = 0
for gh in f:
    for i in range(1,len(gh)-2):
        if (gh[i] == gh[i-1]) and (i == 'R'):
            curlen+=1
            if maxlen < curlen:
                maxlen = curlen
print(curlen)