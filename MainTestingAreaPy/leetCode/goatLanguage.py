class Solution:
    def toGoatLatin(self, S):
        res = ""
        vowels = "aeiou"
        for i, word in enumerate(S.split(' ')):
            if word[0].lower() not in vowels:
                word = word[1:] + word[0]
            word += "ma" + ("a" * (i + 1)) + " "
            res += word
        return res[:len(res) - 1]


sol = Solution()
print(sol.toGoatLatin("I speak Goat Latin"))
