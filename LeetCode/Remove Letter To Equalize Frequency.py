class Solution:
    def equalFrequency(self, word: str) -> bool:
        freqMap = Counter(word)
        for char in word:
            freqMap[char] -= 1
            if freqMap[char] == 0:
                freqMap.pop(char)
            if len(set(freqMap.values())) == 1:
                return True
            freqMap[char] += 1
        return False