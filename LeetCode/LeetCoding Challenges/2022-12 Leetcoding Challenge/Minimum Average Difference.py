class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left, right, minDiff, requiredIndex, n = 0, sum(nums), float('inf'), len(nums), len(nums)
        for index, num in enumerate(nums):
            left += num
            right -= num
            leftAvg = math.floor(left / (index + 1)) if (index + 1) > 0 else 0
            rightAvg = math.floor(right / (n - index - 1)) if (n - index - 1) > 0 else 0
            diff = abs(rightAvg - leftAvg)
            if minDiff > diff:
                minDiff, requiredIndex = diff, index
        return requiredIndex