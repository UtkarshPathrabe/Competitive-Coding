class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaA = abs(ax2 - ax1) * abs(ay2 - ay1)
        areaB = abs(bx2 - bx1) * abs(by2 - by1)
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        xOverlap = right - left
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        yOverlap = top - bottom
        areaOfOverlap = 0
        if xOverlap > 0 and yOverlap > 0:
            areaOfOverlap = xOverlap * yOverlap
        return areaA + areaB - areaOfOverlap