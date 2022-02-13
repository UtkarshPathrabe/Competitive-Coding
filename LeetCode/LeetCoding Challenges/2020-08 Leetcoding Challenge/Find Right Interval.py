class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        hashMap = dict()
        endIntervals = []
        result = []
        for index, interval in enumerate(intervals):
            hashMap[tuple(interval)] = index
            endIntervals.append(interval)
            result.append(-1)
        intervals.sort(key = lambda x : x[0])
        endIntervals.sort(key = lambda x : x[1])
        j = 0
        numberOfIntervals = len(intervals)
        for i, endInterval in enumerate(endIntervals):
            while j < numberOfIntervals and intervals[j][0] < endInterval[1]:
                j += 1
            result[hashMap[tuple(endInterval)]] = -1 if j == numberOfIntervals else hashMap[tuple(intervals[j])]
        return result