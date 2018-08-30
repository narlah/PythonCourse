def valuableExpression(hand):
    hand.sort(reverse=True)
    mE = hand.count("*")
    m = hand.count("-")
    p = hand.count("+")
    hand = hand[0:-mE - m - p]
    minuses, pluses = 0, 0
    if m > 0:
        minuses = sum(int(w) for w in hand[-m:])
        hand = hand[0:-m]
    if p > 0:
        pluses = sum(int(w) for w in hand[-p:])
        hand = hand[0:-p]
    if mE == 1:
        s1, s2 = [hand[0]], [hand[1]]
        for i in range(2, len(hand)):
            if int("".join(s1)) >= int("".join(s2)):
                s2.append(hand[i])
            else:
                s1.append(hand[i])
        r = int("".join(s1)) * int("".join(s2))
    else:
        r = int("".join(hand))
    return int((r + pluses - minuses) % (10 ** 9 + 7))


# 672069074 right
# 679023084 fail
print(valuableExpression(
    ["9", "7", "9", "0", "+", "+", "8", "-", "+", "-", "+", "+", "9", "7", "3", "7", "*", "+", "6", "7", "3", "+", "-",
     "5", "2", "5", "5", "6", "0", "6", "+", "+", "-", "8", "8", "-", "8", "2", "1", "2", "1", "1"]))
