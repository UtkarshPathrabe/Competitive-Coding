class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        oddCount = diff >> 1
        return oddCount if (high & 1 == 0 and low & 1 == 0) else oddCount + 1