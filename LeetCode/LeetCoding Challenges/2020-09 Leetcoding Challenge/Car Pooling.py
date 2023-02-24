class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tripOccupancy = [0] * 1002
        for trip in trips:
            tripOccupancy[trip[1]] += trip[0]
            tripOccupancy[trip[2]] -= trip[0]
        occupancy = 0
        for occupancyDelta in tripOccupancy:
            occupancy += occupancyDelta
            if occupancy > capacity:
                return False
        return True