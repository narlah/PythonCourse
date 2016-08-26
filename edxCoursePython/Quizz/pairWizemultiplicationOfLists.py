def dotProduct(listA, listB):
    index = 0
    resultSum = 0
    while index < len(listA):
        resultSum += listA[index] * listB[index]
        index += 1
    return resultSum


print dotProduct([1, 2, 3], [4, 5, 6])
print dotProduct([-12,0], [1,-1])
