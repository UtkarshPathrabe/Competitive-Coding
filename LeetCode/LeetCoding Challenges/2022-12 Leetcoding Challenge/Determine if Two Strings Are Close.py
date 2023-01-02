class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1Frequency, word2Frequency = Counter(word1), Counter(word2)
        if sorted(word1Frequency.values()) == sorted(word2Frequency.values()) and sorted(word1Frequency.keys()) == sorted(word2Frequency.keys()):
            return True
        return False