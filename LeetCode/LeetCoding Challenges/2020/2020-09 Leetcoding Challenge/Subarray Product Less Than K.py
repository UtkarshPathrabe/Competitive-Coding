class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        product, result, left = 1, 0, 0
        for right, val in enumerate(nums):
            product *= val
            while product >= k:
                product /= nums[left]
                left += 1
            result += right - left + 1
        return result