class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        minDistance, word1Index, word2Index = len(words), -1, -1
        for index, word in enumerate(words):
            if word == word1:
                word1Index = index
            elif word == word2:
                word2Index = index
            if word1Index != -1 and word2Index != -1:
                minDistance = min(minDistance, abs(word2Index - word1Index))
        return minDistance