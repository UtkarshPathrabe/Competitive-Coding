from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stream = SortedList()
        self.size = 0

    def addNum(self, num: int) -> None:
        self.stream.add(num)
        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            midIndex = self.size // 2
            return (self.stream[midIndex] + self.stream[midIndex - 1]) / 2
        else:
            return self.stream[self.size // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()