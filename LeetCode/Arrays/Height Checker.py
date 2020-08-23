class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heightsCopy = sorted(list(heights))
        swapsRequired = 0
        for i in range(len(heights)):
            if heights[i] != heightsCopy[i]:
                swapsRequired += 1
        return swapsRequired