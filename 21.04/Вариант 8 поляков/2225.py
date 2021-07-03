x =  9**7 + 3**21 - 9
l = []
def convert(num):
    if (num == 0):
        return l
    dig = num % 3
    l.append(dig)
    convert(num // 3)

convert(x)
l.reverse()
str1 = ''.join(str(e) for e in l)
print(str1)
