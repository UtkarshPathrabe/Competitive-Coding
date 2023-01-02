class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        endTimeHeap, numberOfRooms = [], 0
        for start, end in intervals:
            if not endTimeHeap or start < endTimeHeap[0]:
                numberOfRooms += 1
            if endTimeHeap and start >= endTimeHeap[0]:
                heappop(endTimeHeap)
            heappush(endTimeHeap, end)
        return numberOfRooms