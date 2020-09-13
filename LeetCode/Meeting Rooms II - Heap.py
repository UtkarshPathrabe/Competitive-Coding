class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x[0])
        occupiedRooms = []
        heappush(occupiedRooms, intervals[0][1])
        for interval in intervals[1:]:
            if occupiedRooms[0] <= interval[0]:
                heappop(occupiedRooms)
            heappush(occupiedRooms, interval[1])
        return len(occupiedRooms)