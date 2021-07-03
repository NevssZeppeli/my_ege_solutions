the_line = ""
max_repeat_number = 0
file = open('24-164.txt')
for line in file:
    m_repeats = 0
    m_letter = ''

    repeats = 0
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            repeats += 1
        else:
            if repeats > m_repeats:
                m_repeats = repeats
                m_letter = line[i-1]
            repeats = 1
    #print(m_letter, m_repeats)
    if m_repeats > max_repeat_number:
        max_repeat_number = m_repeats
        the_line = line
file.close()
c = [0] * 26
for letter in the_line:
    alphabet_index = ord(letter) - ord('A')
    if 0 <= alphabet_index <= 25:
        c[alphabet_index] += 1
the_most_frequent_letter_in_the_line = chr(ord('A') + c.index(max(c)))
file = open('24-164.txt')
number = file.read().count(the_most_frequent_letter_in_the_line)
print(the_most_frequent_letter_in_the_line, number)
