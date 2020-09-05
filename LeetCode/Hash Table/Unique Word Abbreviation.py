class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.hashMap = defaultdict(set)
        for word in dictionary:
            abbr = self._getAbbr(word)
            self.hashMap[abbr].add(word)

    def isUnique(self, word: str) -> bool:
        abbr = self._getAbbr(word)
        words = self.hashMap[abbr]
        return len(words) == 0 or (len(words) == 1 and word in words)
    
    def _getAbbr(self, word):
        wordLen = len(word)
        return word if wordLen <= 2 else word[0] + str(wordLen - 2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)