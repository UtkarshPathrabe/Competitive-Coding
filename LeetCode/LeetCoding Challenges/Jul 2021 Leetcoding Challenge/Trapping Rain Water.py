class Solution:
    def trap(self, height: List[int]) -> int:
        result, left, right, leftMax, rightMax = 0, 0, len(height) - 1, 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    result += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    result += rightMax - height[right]
                right -= 1
        return result