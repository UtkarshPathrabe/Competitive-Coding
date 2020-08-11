class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.sum = 0
        self.capacity = 0

    def next(self, val: int) -> float:
        if self.capacity == self.size:
            tempValue = self.queue.popleft()
            self.sum -= tempValue
            self.capacity -= 1
        self.queue.append(val)
        self.sum += val
        self.capacity += 1
        return self.sum / self.capacity


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)