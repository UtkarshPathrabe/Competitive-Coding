class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        def isConsistent(word: str):
            wordSet = set(word)
            for char in wordSet:
                if char not in allowedSet:
                    return False
            return True
        result = 0
        for word in words:
            if isConsistent(word):
                result += 1
        return result