class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        left, right = 1, len(nums) - 2
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            first = mid
            if nums[mid - 1] == nums[mid]:
                first = mid - 1
            if first & 1 == 0:
                left = first + 2
            else:
                right = first - 1