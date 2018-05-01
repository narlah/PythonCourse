import random


def calculateHashKey(a1):
    return sum(a1[j] * (5 ^ j) for j in range(10))


def finish():
    print(str(len(attempts)) + "\n")
    print()
    for x in attempts:
        print(x, attempts[x])


cards = [i for i in range(1, 53)]
attempts = {}
limitForSimilarity = 15
flag = 0
for i in range(10000000):
    cardCopy = cards[:]
    random.shuffle(cardCopy)
    hashKey = calculateHashKey(cardCopy)
    flag += 1
    if hashKey in attempts:
        print(hashKey, attempts[hashKey])
        print("Collision : \n hash : " + str(hashKey) + "\n" + str(cardCopy) + "\n" + str(attempts[hashKey]) + "\n")
        cards1 = cardCopy[:limitForSimilarity]
        attemptCards1 = attempts[hashKey][:limitForSimilarity]
        print("attempt ", calculateHashKey(cards1), cards1)
        print("in dict ", calculateHashKey(attemptCards1), attemptCards1)
        finish()
        break
    attempts[hashKey] = cardCopy
    if flag == 50000:
        print(i)
        flag = 0
