class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result, N, i = [], len(intervals), 0
        while i < N:
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                j = i
                while j < N:
                    result.append(intervals[j])
                    j += 1
                return result
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            i += 1
        result.append(newInterval)
        return result
            