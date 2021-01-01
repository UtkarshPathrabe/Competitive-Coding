class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        characterSet = set()
        for c in s:
            if c in characterSet:
                characterSet.remove(c)
            else:
                characterSet.add(c)
        return len(characterSet) <= 1