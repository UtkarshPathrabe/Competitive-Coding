class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x : x[1])
        arrows, end = 1, points[0][1]
        for xStart, xEnd in points[1:]:
            if xStart > end:
                arrows += 1
                end = xEnd
        return arrows