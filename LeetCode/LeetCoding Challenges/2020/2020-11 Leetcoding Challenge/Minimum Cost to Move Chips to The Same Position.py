class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0
        for pos in position:
            if pos % 2:
                odd += 1
            else:
                even += 1
        return min(odd, even)