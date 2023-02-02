class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def calculateSlope(x1, y1, x2, y2):
            return (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
        result = 1
        for i in range(len(points)):
            slopes = Counter()
            currentMaximum = 1
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                slope = calculateSlope(x1, y1, x2, y2)
                slopes[slope] += 1
                currentMaximum = max(currentMaximum, 1 + slopes[slope])
            result = max(result, currentMaximum)
        return result