def f(x):
    import math
    return 400 * math.e ** (math.log(0.5) / 3.66 * x)


def radiationExposure(start, stop, step):
    count = 0.0
    indexS, indexE = start, stop
    while indexS < indexE:
        count += f(indexS) * step
        indexS += step
    return count


print radiationExposure(0, 4, 0.25)
