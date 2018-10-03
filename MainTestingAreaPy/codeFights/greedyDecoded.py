def greedyDecoding(m): #defood solution , not mine https://app.codesignal.com/challenge/JhtBKjkeDwaaERovM/solutions/mJne4FS4ArY532xSZ
    m = str(m)
    a = ''
    while m:
        i = [1, 2][m[:2] < '27']
        a += chr(64 + int(m[:i]))
        m = m[i:]
    return a


print(greedyDecoding(195318520))
