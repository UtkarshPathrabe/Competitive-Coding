class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap, maxLen, count = {0: -1}, 0, 0
        for i in range(len(nums)):
            count += (-1 if nums[i] == 0 else 1)
            if count in hashMap:
                maxLen = max(maxLen, i - hashMap[count])
            else:
                hashMap[count] = i
        return maxLen