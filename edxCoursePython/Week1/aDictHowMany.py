def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    index = 0
    key = ''
    for k in aDict.keys():
        if len(aDict[k]) > index:
            index = len(aDict[k])
            key = k
    return key


print(biggest({'g': [], 'k': [], 'y': [3, 4, 15, 14], 't': [], 'Y': [], 'X': [3, 11, 3]}))
