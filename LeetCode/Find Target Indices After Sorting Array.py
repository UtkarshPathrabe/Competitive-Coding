class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for index, num in enumerate(nums):
            if num == target:
                result.append(index)
        return result