class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left, right = 0, len(colors) - 1
        while colors[0] == colors[right]:
            right -= 1
        while colors[-1] == colors[left]:
            left += 1
        return max(len(colors) - 1 - left, right)