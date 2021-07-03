import doctest

def factorize(x):
    """ Раскладывает число на простые множители.

    >>> factorize(100)
    [2, 2, 5, 5]
    >>> factorize(72)
    [2, 2, 2, 3, 3]
    >>> factorize(627)
    [3, 11, 19]
    >>> factorize(5)
    [5]
    """
    divs = []
    while x % 2 == 0:
        divs.append(2)
        x //= 2
    d = 3
    while d*d <= x:
        if x % d == 0:
            x //= d
            divs.append(d)
        else:
            d += 2
    divs.append(x)
    return divs


n = 0
last = None
for x in range(105673, 220784 + 1):
    divs = factorize(x)
    if len(divs) == 3 and len(set(divs)) == 3:
        n += 1
        last = x
print(n, last)

doctest.testmod()
