class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        computeQuotientSum = lambda x : sum([ceil(num / x) for num in nums])
        left, right = 1, nums[-1]
        while left <= right:
            pivot = left + ((right - left) >> 1)
            currentSum = computeQuotientSum(pivot)
            if currentSum > threshold:
                left = pivot + 1
            else:
                right = pivot - 1
        return left