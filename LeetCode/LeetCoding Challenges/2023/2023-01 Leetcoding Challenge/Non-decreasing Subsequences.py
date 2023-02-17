class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result, N = set(), len(nums)
        currList = []
        def helper(index: int):
            if index == N:
                if len(currList) > 1:
                    result.add(tuple(currList))
                return
            if not currList or nums[index] >= currList[-1]:
                currList.append(nums[index])
                helper(index + 1)
                currList.pop()
            helper(index + 1)
        helper(0)
        return result