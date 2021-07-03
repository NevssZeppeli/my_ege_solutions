def max_successive_abc_pairs(line):
    num = 0
    old_letter = '?'
    for letter in line:
        if ord(letter) - ord(old_letter) == 1:
            num += 1
        old_letter = letter
    return num


fname = 'test.txt' #'24-s1.txt'
f = open(fname)
sorted_lines = sorted((line.strip() for line in f),
                      =max_successive_abc_pairs)
print(sorted_lines[-1])
