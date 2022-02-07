class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.sum = 0
        self.itemsInQueue = 0

    def next(self, val: int) -> float:
        self.sum += val
        self.queue.append(val)
        self.itemsInQueue += 1
        if self.itemsInQueue > self.size:
            top = self.queue.popleft()
            self.sum -= top
            self.itemsInQueue -= 1
        return self.sum / self.itemsInQueue


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)