class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result, currentSum, hashSet, start = 0, 0, set(), 0
        for end in range(len(nums)):
            while nums[end] in hashSet:
                hashSet.remove(nums[start])
                currentSum -= nums[start]
                start += 1
            currentSum += nums[end]
            hashSet.add(nums[end])
            result = max(result, currentSum)
        return result