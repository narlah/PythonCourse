def findPairs(arr, x):
    hash = set()
    for e in arr:
        s = x - e
        if s in hash:
            return True
        hash.add(s)
    return False


def findPairsLinear(arr, x):
    l = 0
    r = len(arr)-1
    while (l < r):
        m = arr[l] + arr[r]
        if m == x:
            return True
        if m < x:
            l += 1
        else:
            r -= 1
    return False


print(findPairs([1, 2, 4, 4], 8))
print(findPairsLinear([1, 2, 4, 4], 8))
