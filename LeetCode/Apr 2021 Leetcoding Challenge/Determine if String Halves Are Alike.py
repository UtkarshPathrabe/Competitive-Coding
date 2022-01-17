class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        def getNumberOfVowels(s):
            numberOfVowels = 0
            for char in s:
                if char in vowels:
                    numberOfVowels += 1
            return numberOfVowels
        return getNumberOfVowels(s[:len(s) // 2]) == getNumberOfVowels(s[len(s) // 2:])