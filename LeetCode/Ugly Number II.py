class Ugly:
    def __init__(self):
        self.nums = nums = [1,]
        i2, i3, i5 = 0, 0, 0
        for _ in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)
            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1

class Solution:
    ugly = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.ugly.nums[n - 1]