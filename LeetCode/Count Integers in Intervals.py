from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.currentCount = 0
        self.intervals = SortedList()

    def add(self, left: int, right: int) -> None:
        k = self.intervals.bisect_left((left, right))
        while k < len(self.intervals) and self.intervals[k][0] <= right:
            l, r = self.intervals.pop(k)
            self.currentCount -= r - l + 1
            right = max(right, r)
        if k and self.intervals[k - 1][1] >= left:
            l, r = self.intervals.pop(k - 1)
            self.currentCount -= r - l + 1
            left, right = l, max(right, r)
        self.currentCount += right - left + 1
        self.intervals.add((left, right))

    def count(self) -> int:
        return self.currentCount


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()