class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freqMap = Counter(text)
        return min(freqMap['b'], freqMap['a'], freqMap['n'], freqMap['l'] // 2, freqMap['o'] // 2)