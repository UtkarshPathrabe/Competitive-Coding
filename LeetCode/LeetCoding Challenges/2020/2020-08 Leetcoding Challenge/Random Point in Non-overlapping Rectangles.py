class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.pSum = []
        self.total = 0
        for x in rects:
            self.total += ((x[2] - x[0] + 1) * (x[3] - x[1] + 1))
            self.pSum.append(self.total)

    def pick(self) -> List[int]:
        target = random.randrange(self.total)
        low, high = 0, len(self.rects) - 1
        while low < high:
            mid = low + (high - low) // 2
            if target >= self.pSum[mid]:
                low = mid + 1
            else:
                high = mid
        rect = self.rects[low]
        width, height = rect[2] - rect[0] + 1, rect[3] - rect[1] + 1
        base = self.pSum[low] - (width * height)
        return [rect[0] + ((target - base) % width), rect[1] + ((target - base) // width)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()