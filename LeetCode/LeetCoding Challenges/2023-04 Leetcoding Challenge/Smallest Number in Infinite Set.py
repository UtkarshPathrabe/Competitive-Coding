class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.heap = [self.smallest,]
        self.hashSet = set([self.smallest,])

    def popSmallest(self) -> int:
        num = heapq.heappop(self.heap)
        self.hashSet.remove(num)
        self.smallest += 1
        self.addBack(self.smallest)
        return num

    def addBack(self, num: int) -> None:
        if num not in self.hashSet:
            heapq.heappush(self.heap, num)
        self.hashSet.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)