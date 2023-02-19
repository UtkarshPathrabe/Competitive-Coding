class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = [float('-inf')] + heaters[::] + [float('inf')]
        heaters.sort()
        houses.sort()
        result = float('-inf')
        for house in houses:
            i = bisect.bisect_left(heaters, house)
            distance = min(house - heaters[i - 1], heaters[i] - house)
            result = max(result, distance)
        return result