class Solution:

    def __init__(self, w: List[int]):
        self.prefixSums = [0] * len(w)
        self.prefixSums[0] = w[0]
        for i in range(1, len(w)):
            self.prefixSums[i] = self.prefixSums[i - 1] + w[i]

    def pickIndex(self) -> int:
        target = self.prefixSums[-1] * random.random()
        low, high = 0, len(self.prefixSums)
        while low < high:
            pivot = low + ((high - low) >> 1)
            if self.prefixSums[pivot] < target:
                low = pivot + 1
            else:
                high = pivot
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()