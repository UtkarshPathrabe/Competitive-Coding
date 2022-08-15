class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result, brokenSet = 0, set(brokenLetters)
        for word in text.split(' '):
            invalid = False
            for char in word:
                if char in brokenSet:
                    invalid = True
                    break
            if not invalid:
                result += 1
        return result