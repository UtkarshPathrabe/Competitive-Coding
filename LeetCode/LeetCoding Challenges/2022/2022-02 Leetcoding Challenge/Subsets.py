class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, numsCapacity = [], len(nums)
        def backtrack(currentSet, startIndex):
            result.append(list(currentSet))
            for i in range(startIndex, numsCapacity):
                currentSet.append(nums[i])
                backtrack(currentSet, i + 1)
                currentSet.pop()
        backtrack([], 0)
        return result