class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxDiff = float('-inf')
        for i in range(1, len(points)):
            maxDiff = max(maxDiff, points[i][0] - points[i - 1][0])
        return maxDiff