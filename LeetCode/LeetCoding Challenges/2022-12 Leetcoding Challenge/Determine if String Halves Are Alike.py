class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def isVowel(char):
            return char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        def getNumberOfVowels(s):
            count = 0
            for char in s:
                count += (1 if isVowel(char) else 0)
            return count
        return getNumberOfVowels(s[ : len(s) // 2]) == getNumberOfVowels(s[len(s) // 2 : ])