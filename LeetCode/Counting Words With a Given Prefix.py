class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for word in words:
            result += 1 if word.startswith(pref) else 0
        return result