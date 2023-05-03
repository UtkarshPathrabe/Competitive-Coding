from sortedcontainers import SortedSet

class SummaryRanges:

    def __init__(self):
        self._values = SortedSet()

    def addNum(self, value: int) -> None:
        self._values.add(value)

    def getIntervals(self) -> List[List[int]]:
        if len(self._values) == 0:
            return []
        intervals, left, right = [], -1, -1
        for value in self._values:
            if left < 0:
                left = right = value
            elif value == right + 1:
                right = value
            else:
                intervals.append([left, right])
                left = right = value
        intervals.append([left, right])
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()