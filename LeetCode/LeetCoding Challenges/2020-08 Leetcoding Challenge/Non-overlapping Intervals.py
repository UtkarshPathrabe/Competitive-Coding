class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervalsLength = len(intervals)
        if intervalsLength == 0:
            return 0
        intervals.sort(key = lambda x : x[1])
        count = 1
        end = intervals[0][1]
        for i in range(1, intervalsLength):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1
        return intervalsLength - count