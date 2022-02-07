class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        result = seats.index(1)
        seats.reverse()
        result = max(seats.index(1), result)
        for seat, group in groupby(seats):
            if not seat:
                emptySeatsLength = len(list(group))
                result = max(result, (emptySeatsLength + 1) // 2)
        return result