class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numsCapacity, result = len(nums), []
        def backtrack(startIndex = 0):
            if startIndex == numsCapacity:
                result.append(list(nums))
            for i in range(startIndex, numsCapacity):
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
                backtrack(startIndex + 1)
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
        backtrack()
        return result