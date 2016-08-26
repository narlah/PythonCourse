s = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
given = 10
expected = 79


def findExpected(s, given):
    count = 0
    pos = given
    for char in s[given + 1:]:
        pos += 1
        if char == '(':
            count += 1
        elif (char == ")") & (count == 0):
            return pos
        elif char == ")":
            count -= 1
    return -1


print findExpected(s, given)
