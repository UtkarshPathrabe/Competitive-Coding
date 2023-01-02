class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 not in nums:
            return 1
        if n == 1:
            return 2
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        for i in range(n):
            num = abs(nums[i])
            if num == n:
                nums[0] = - abs(nums[0])
            else:
                nums[num] = - abs(nums[num])
        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n + 1