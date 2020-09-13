class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        occupancyAtTimestamp = [0] * 1001
        for trip in trips:
            occupancyAtTimestamp[trip[1]] += trip[0]
            occupancyAtTimestamp[trip[2]] -= trip[0]
        usedCapacity = 0
        for occupancyChange in occupancyAtTimestamp:
            usedCapacity += occupancyChange
            if usedCapacity > capacity:
                return False
        return True