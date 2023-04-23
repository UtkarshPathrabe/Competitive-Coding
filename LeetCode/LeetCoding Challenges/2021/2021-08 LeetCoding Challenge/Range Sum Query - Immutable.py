class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.sums[i + 1] = self.sums[i] + num

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)