class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, numsCapacity = set(), len(nums)
        def backtrack(currentSubset, startIndex):
            result.add(tuple(currentSubset))
            for i in range(startIndex, numsCapacity):
                currentSubset.append(nums[i])
                backtrack(currentSubset, i + 1)
                currentSubset.pop()
        backtrack([], 0)
        return result