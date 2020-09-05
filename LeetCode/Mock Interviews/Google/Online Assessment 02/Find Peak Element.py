class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        numsLen = len(nums)
        if numsLen == 0:
            return -1
        if numsLen == 1:
            return 0
        if numsLen == 2:
            return 0 if nums[0] > nums[1] else 1
        left, right = 0, numsLen - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left