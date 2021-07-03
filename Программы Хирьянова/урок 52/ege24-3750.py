text = open('24-157.txt').read()
stat = [0]*26  # there are 26 letters from A to Z
it = iter(text)
prev2 = next(it)
prev1 = next(it)
for current in it:
    if prev2 == current:
        if 'A' <= prev1 <= 'Z':
            index = ord(prev1) - ord('A')
            stat[index] += 1
    prev2, prev1 = prev1, current  # shame on me
m_stat = max(stat)
m_index = stat.index(m_stat)
print(chr(ord('A') + m_index), m_stat, sep='')
