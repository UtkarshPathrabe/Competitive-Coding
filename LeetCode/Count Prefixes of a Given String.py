class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        hashSet = set(s[:i] for i in range(1, len(s) + 1))
        result = 0
        for word in words:
            result += 1 if word in hashSet else 0
        return result