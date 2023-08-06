class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        def isVowel(c: str) -> bool:
            return c in 'aeiou'
        
        currLength = 0
        for i in range(k):
            if isVowel(s[i]):
                currLength += 1
        result = currLength
        for i in range(k, len(s)):
            if isVowel(s[i - k]):
                currLength -= 1
            if isVowel(s[i]):
                currLength += 1
            result = max(result, currLength)
        return result
        