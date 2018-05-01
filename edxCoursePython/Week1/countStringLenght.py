


def semordnilap(str1, str2):
    global count
    count += 1
    if len(str1) != len(str2):
        return False
    if len(str1) == 0:
        return True
    if str1[0:1] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False

def test():
    global count
    count =0
    print(semordnilap("semordnilap", "palindromes"))
    print(count)


test()

# def isIn(char, aStr):
#     if len(aStr) == 0:
#         return False
#     if (len(aStr) == 1) & ((aStr[:-1] > char) or (aStr[0] < char)):
#         return False
#     pos = len(aStr) / 2
#     # print char == aStr[pos]
#     # print char + " " + str(aStr[pos])
#     if char == aStr[pos]:
#         return True
#     elif char > aStr[pos]:
#         return isIn(char, aStr[pos:])
#     else:
#         return isIn(char, aStr[:pos])


# print isIn("l", "abcdef")
# def lenRecur(aStr):
#     print aStr
#     return 1 + lenRecur(aStr[1:]) if aStr else 0
#
#
# print lenRecur("baba")
