def getSublists(L=[], n=1):
    result = []
    for l in range(len(L) - n + 1):
        temp = []
        for i in range(n):
            temp.append(L[i + l])
        result.append(temp)
    return result


print(getSublists([5, 2, 4, 1, 3], 1))
