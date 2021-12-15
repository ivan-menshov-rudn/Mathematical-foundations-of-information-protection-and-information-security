import math


def func(x, y):
    return (x ** 2 + 5) % y


c = 1
a = c
b = c
n = 1359331
print(a, b, sep='    ')
while True:
    a = func(a, n) % n
    b = func(func(b, n), n) % n
    d = math.gcd(a - b, n)
    print(a, b, d, sep='    ')
    if 1 < d < n:
        p = d
        print(f'p = {p}')
        break
    elif d == n:
        print('Делитель не найден')
        break
