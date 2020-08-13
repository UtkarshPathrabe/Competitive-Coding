class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        index, n = 0, len(intervals)
        startOfNewInterval, endOfNewInterval = newInterval
        while index < n and intervals[index][0] < startOfNewInterval:
            result.append(intervals[index])
            index += 1
        if not result or result[-1][1] < startOfNewInterval:
            result.append(newInterval)
        else:
            result[-1][1] = max(result[-1][1], endOfNewInterval)
        while index < n:
            start, end = intervals[index]
            if result[-1][1] < start:
                result.append(intervals[index])
            else:
                result[-1][1] = max(result[-1][1], end)
            index += 1
        return result