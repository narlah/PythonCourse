def flatten(aList):
    result = []
    for item in aList:
        if type(item) is list:
            for subelement in flatten(item):
                result.append(subelement)
        else:
            result.append(item)
    return result


print flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5])
print flatten([])
print flatten([1])
print flatten([[1]])
print flatten([[], [1], [1, 2]])
print flatten(["blq"])
print flatten([["blq"],[1],[],[[]]])
