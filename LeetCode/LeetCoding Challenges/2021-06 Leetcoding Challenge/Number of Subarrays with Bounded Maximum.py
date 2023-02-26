class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            result = c = 0
            for num in nums:
                c = c + 1 if num <= bound else 0
                result += c
            return result
        return count(right) - count(left - 1)