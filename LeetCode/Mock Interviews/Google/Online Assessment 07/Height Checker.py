class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        targetArray = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != targetArray[i]:
                result += 1
        return result