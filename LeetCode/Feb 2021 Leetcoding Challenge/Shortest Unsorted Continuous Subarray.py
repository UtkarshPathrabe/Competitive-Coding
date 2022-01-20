class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        currentMin, currentMax, flag, l, r = float('inf'), float('-inf'), False, 0, len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                currentMin = min(currentMin, nums[i])
        flag = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                currentMax = max(currentMax, nums[i])
        while l < len(nums):
            if currentMin < nums[l]:
                break
            l += 1
        while r > -1:
            if currentMax > nums[r]:
                break
            r -= 1
        return 0 if r - l < 0 else r - l + 1