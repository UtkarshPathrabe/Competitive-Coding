class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        count, prevEnd = 0, 0
        for _, end in intervals:
            if end > prevEnd:
                count += 1
                prevEnd = end
        return count