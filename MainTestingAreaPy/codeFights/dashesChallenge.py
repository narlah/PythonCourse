# NOT MINE

def dashes(n, *r):
    t = "-"
    while n:
        n -= 1
        r += " " * n + t + " " * n,
        t += "|-"
    return r + r[-2::-1]


dashes2 = lambda n: [' ' * i + '-|' * (n + ~i) + '-' + ' ' * i for i in map(abs, range(1 - n, n))]

print(dashes(4))

print(dashes2(4))