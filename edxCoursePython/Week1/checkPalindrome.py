def isPalindrome(aString):
    if len(aString) < 2:
        return True
    if aString[0:1] == aString[len(aString) - 1: len(aString)]:
        return isPalindrome(aString[1:len(aString) - 1])
    else:
        return False

text = "Are we not drawn onward, we few, drawn onward to new era?"
line = text.translate(None, '!@#$,? ').lower()
print line
print isPalindrome("sBmHhyKa")
