class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = set(nums[0])
        for num in nums[1:]:
            result = result.intersection(set(num))
        return sorted(result)