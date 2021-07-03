y =  (((9**22) + (3 ** 66) - 18))
c=0

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

for x in ternary(y):
    if x == '2':
        c+=1
print(c)