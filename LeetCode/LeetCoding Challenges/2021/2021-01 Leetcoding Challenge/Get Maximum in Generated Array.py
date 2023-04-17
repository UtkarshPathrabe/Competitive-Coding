class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        maximumValue, nums[1] = 1, 1
        for i in range(1, n // 2 + 1):
            nums[i * 2] = nums[i]
            if i * 2 + 1 <= n:
                nums[i * 2 + 1] = nums[i] + nums[i + 1]
                maximumValue = max(maximumValue, nums[i * 2 + 1])
        return maximumValue