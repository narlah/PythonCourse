def findPairs(arr, x):
    hash = set()
    for e in arr:
        if e in hash:
            return True
        hash.add(x - e)
    return False


def findPairsLinear(arr, x):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = arr[l] + arr[r]
        if m == x:
            return True
        if m < x:
            l += 1
        else:
            r -= 1
    return False


def findTriplets(arr, x):
    l = len(arr)
    for i in range(l - 2):
        m = x - arr[i]
        if findPairs(arr[i+1: l], m):
            return True
    return False


print(findPairs([1, 2, 4, 4], 8))
print(findPairsLinear([1, 2, 4, 4], 8))
print(findTriplets([1, 17, 4, 5, 7, 8, 9], 8))
