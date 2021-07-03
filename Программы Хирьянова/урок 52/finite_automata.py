alpha = ''.join(chr(ord('А') + i) for i in range(32)) + 'Ё'
alpha = alpha + alpha.lower()

line = input()
state = 0
for c in line:
    if state == 0:
        if c in alpha:
            state = 1
            word = c
    elif state == 1:
        if c in alpha:
            word += c
        else:
            state = 0
            print(word)
        
