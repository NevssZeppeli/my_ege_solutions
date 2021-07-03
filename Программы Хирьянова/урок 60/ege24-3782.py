file = open('24-s1.txt')
lines = file.readlines()
qline = ""
for line in lines:
    if line.count('Q') >= qline.count('Q'):
        qline = line
letters = sorted(set(qline.strip()))
mletter = letters[0]
for letter in letters:
    if qline.count(letter) < qline.count(mletter):
        mletter = letter
print(min(letters, key=qline.count))
print(mletter, ''.join(lines).count(mletter))

# однострочник от Александра:
print(f"{(ml := min(sorted({l: c for l in __import__('string').ascii_uppercase if (c := (s := __import__('functools').reduce(lambda p, c: c if c.count('Q') >= p.count('Q') else p, (text := (text := open('24-s1.txt').readlines())))).strip().count(l)) > 0}.items(), key=lambda x: x[0]), key=lambda x: x[1])[0])}{''.join(text).count(ml)}")


    

    
