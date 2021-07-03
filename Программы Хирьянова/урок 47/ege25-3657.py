1# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3657
# [1000000; 1300000]
# все цифры меньше 3, а сумма цифр кратна 10
# отобрать каждое десятое в порядке возрастания,
# справа укажите кол-во его собственных делителей
A = []
for x in range(1000000, 1300000+1):
    if (all(digit in "012" for digit in str(x)) and
        sum(int(digit) for digit in str(x)) % 10 == 0):
        A.append(x)
B = A[9::10]  # каждое десятое число
for x in B:
    num_divs = 0
    for div in range(2, x):
        if x % div == 0:
            num_divs += 1
    print(x, num_divs)
