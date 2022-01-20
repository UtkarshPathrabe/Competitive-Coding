class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        totalDistance, currentDist, i = sum(distance), 0, start
        while i != destination:
            currentDist += distance[i]
            i = (i + 1) % len(distance)
        return min(currentDist, totalDistance - currentDist)