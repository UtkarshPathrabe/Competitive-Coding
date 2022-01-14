class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, area = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                area = max(area, height[i] * (j - i))
                i += 1
            else:
                area = max(area, height[j] * (j - i))
                j -= 1
        return area