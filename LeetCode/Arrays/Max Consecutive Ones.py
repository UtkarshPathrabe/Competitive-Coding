class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        oneCount, maxOneCount = 0, 0
        for num in nums:
            if num == 1:
                oneCount += 1
            else:
                oneCount = 0
            maxOneCount = max(maxOneCount, oneCount)
        return maxOneCount