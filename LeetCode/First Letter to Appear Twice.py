class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashSet = set()
        for c in s:
            if c in hashSet:
                return c
            hashSet.add(c)