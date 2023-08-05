class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        currentSum, avgRange, N = 0, 2 * k + 1, len(nums)
        result = [-1] * N
        if N < avgRange:
            return result
        for i in range(avgRange):
            currentSum += nums[i]
        for i in range(k, N - k):
            result[i] = currentSum // avgRange
            currentSum += (nums[i + k + 1] - nums[i - k]) if i != N - k - 1 else 0
        return result