class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximumArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maximumArea = max(maximumArea, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximumArea