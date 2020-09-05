class NumArray:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.nums = nums
        self.sumArray = [0]
        for num in nums:
            self.sumArray.append(self.sumArray[-1] + num)

    def update(self, i: int, val: int) -> None:
        oldValue = self.nums[i]
        self.nums[i] = val
        for index in range(i, self.size):
            self.sumArray[index + 1] += (val - oldValue)

    def sumRange(self, i: int, j: int) -> int:
        return self.sumArray[j + 1] - self.sumArray[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)