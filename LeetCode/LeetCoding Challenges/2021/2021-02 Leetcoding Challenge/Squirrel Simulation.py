class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def distance(a, b):
            return abs(a[1] - b[1]) + abs(a[0] - b[0])
        def distanceToTree(nut):
            return distance(nut, tree)
        def distanceToSquirrel(nut):
            return distance(nut, squirrel)
        totalDistance, maxSaving = 0, float('-inf')
        for nut in nuts:
            d = distanceToTree(nut)
            totalDistance += (d * 2)
            maxSaving = max(maxSaving, d - distanceToSquirrel(nut))
        return totalDistance - maxSaving