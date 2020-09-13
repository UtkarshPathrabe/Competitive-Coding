class Solution:
    def minFlips(self, target: str) -> int:
        return len([i[0] for i in groupby('0' + target)]) - 1