fname = '24-s1.txt' # 'test.txt' 
f = open(fname)
m_line = ""
m_num = 0
for line in f:
    num = 0
    old_letter = '?'
    for letter in line:
        if ord(letter) - ord(old_letter) == 1:
            num += 1
        old_letter = letter
    if num >= m_num:
        m_num = num
        m_line = line
print(m_line)
ABC = ''.join(chr(ord('A') + i) for i in range(26))
F = [m_line.count(letter) for letter in ABC]
min_existing_counter = (min(x for x in F if x != 0))
the_letter_index = F.index(min_existing_counter)
the_letter = chr(ord('A') + the_letter_index)
print(the_letter)
print(open(fname).read().count(the_letter))
