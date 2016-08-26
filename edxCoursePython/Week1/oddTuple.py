def oddTuples(aTup):
    if len(aTup) == 0 or len(aTup) == 1:
        return aTup
    z = 1
    returnTuple = aTup[0:1]
    for k in aTup[1:]:
        if z % 2 == 0:
            returnTuple=returnTuple + (k,)
        z += 1
    return returnTuple


print oddTuples((5, 1, 3, 1, 3, 10, 12))
