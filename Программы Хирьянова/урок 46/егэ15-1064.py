#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=1064
#(x + 3y ≠ 27) ∨ ((A > x) ∧ (A > y))
universum = range(0, 1000)
A = 1
while not all(x + 3*y != 27 or (A > x and A > y)
              for x in universum
              for y in universum):
    A += 1
print(A)
