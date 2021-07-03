def count_all(src):
    counters = {}
    for counter, item in enumerate(src):
        counters[item] = counters.get(item, 0) + 1
    return counters


print(count_all(["cat", "dog", "cat"]))
# {"cat": 2, "dog": 1}
print(count_all("hello"))
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(count_all("*" * 20))
# {'*': 20}
print(count_all([]))
# {}