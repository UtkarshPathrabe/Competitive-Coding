class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index, intervalsCapacity, startOfNewInterval, endOfNewInterval, result = 0, len(intervals), newInterval[0], newInterval[1], []
        while index < intervalsCapacity and intervals[index][0] < startOfNewInterval:
            result.append(intervals[index])
            index += 1
        if not result or result[-1][1] < startOfNewInterval:
            result.append(newInterval)
        else:
            result[-1][1] = max(result[-1][1], endOfNewInterval)
        while index < intervalsCapacity:
            if result[-1][1] < intervals[index][0]:
                result.append(intervals[index])
            else:
                result[-1][1] = max(result[-1][1], intervals[index][1])
            index += 1
        return result