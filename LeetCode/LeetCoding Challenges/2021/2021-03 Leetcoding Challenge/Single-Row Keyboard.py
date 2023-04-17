class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indexMap, result, prevIndex = {}, 0, 0
        for index, char in enumerate(keyboard):
            indexMap[char] = index
        for char in word:
            result += abs(indexMap[char] - prevIndex)
            prevIndex = indexMap[char]
        return result