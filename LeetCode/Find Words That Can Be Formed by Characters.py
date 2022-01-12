class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        charFreq = Counter(chars)
        def isGood(word: str) -> bool:
            wordCharFreq = Counter(word)
            for key, val in wordCharFreq.items():
                if key not in charFreq or charFreq[key] < val:
                    return False
            return True
        for word in words:
            if isGood(word):
                result += len(word)
        return result