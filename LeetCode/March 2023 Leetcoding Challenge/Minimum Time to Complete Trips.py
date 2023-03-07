class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def canCompleteTrips(givenTime: int) -> bool:
            tripCount = 0
            for t in time:
                tripCount += (givenTime // t)
            return tripCount >= totalTrips
        low, high, result = 1, totalTrips * max(time), totalTrips * max(time)
        while low <= high:
            mid = (low + high) >> 1
            if canCompleteTrips(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result