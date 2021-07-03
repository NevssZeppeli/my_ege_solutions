s = "1"*2019 + "2"*2119
while "222" in s:
    s = s.replace("222", "1", 1)
    s = s.replace("111", "2", 1)
print(s)
