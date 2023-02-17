class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])
        horizontalCuts.sort()
        verticalCuts.sort()
        hMax, vMax = 0, 0
        for i in range(1, len(horizontalCuts)):
            hMax = max(horizontalCuts[i] - horizontalCuts[i - 1], hMax)
        for i in range(1, len(verticalCuts)):
            vMax = max(verticalCuts[i] - verticalCuts[i - 1], vMax)
        return (hMax * vMax) % (1000000000 + 7)