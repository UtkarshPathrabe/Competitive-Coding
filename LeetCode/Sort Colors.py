class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        right0 = current = 0
        left2 = numsLen - 1
        while current <= left2:
            if nums[current] == 0:
                nums[current], nums[right0] = nums[right0], nums[current]
                current += 1
                right0 += 1
            elif nums[current] == 2:
                nums[current], nums[left2] = nums[left2], nums[current]
                left2 -= 1
            else:
                current += 1