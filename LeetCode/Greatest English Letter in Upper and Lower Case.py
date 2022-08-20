from string import ascii_uppercase as auc

class Solution:
    def greatestLetter(self, s: str) -> str:
        hashSet = set(s)
        for char in reversed(auc):
            if char in hashSet and char.lower() in hashSet:
                return char
        return ''