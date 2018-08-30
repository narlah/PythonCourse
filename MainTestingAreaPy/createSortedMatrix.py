import random


def squareMatrix(x, y, maxLen):
    arr = [[]]
    items = [(0,0)]
    current = 0
    for i in range(x):
        l = ''
        for j in range(y):
            r = random.randint(current+1, min(maxLen, current + 10))
            if r > current:
                current = r
            l = str(l) + str(r) + (6 - len(str(r)))*" "
        current =0
        print(l)

random.seed(1)
squareMatrix(20, 20, 200)
