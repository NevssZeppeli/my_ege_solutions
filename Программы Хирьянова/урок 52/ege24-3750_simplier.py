text = open('24-157.txt').read()
stat = [0]*26  # there are 26 letters from A to Z
for i in range(1, len(text) - 1):
    if text[i-1] == text[i+1]:
        if 'A' <= text[i] <= 'Z':
            index = ord(text[i]) - ord('A')
            stat[index] += 1
m_stat = max(stat)
m_index = stat.index(m_stat)
print(chr(ord('A') + m_index), m_stat, sep='')
