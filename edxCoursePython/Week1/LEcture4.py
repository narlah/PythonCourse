def a(x, y, z):
    if x:
        return y
    else:
        return z


def b(q, r):
    return a(q > r, q, r)


print(b(3, 2))
