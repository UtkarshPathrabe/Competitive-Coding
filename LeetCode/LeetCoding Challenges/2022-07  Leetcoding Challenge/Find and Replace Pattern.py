class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            hashMap = {}
            for x, y in zip(pattern, word):
                if hashMap.setdefault(x, y) != y:
                    return False
            return len(set(hashMap.values())) == len(hashMap.values())
        return filter(match, words)