class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        for start, end in intervals:
            if start < toBeRemoved[0]:
                result.append([start, min(end, toBeRemoved[0])])
            if toBeRemoved[1] < end:
                result.append([max(start, toBeRemoved[1]), end])
        return result