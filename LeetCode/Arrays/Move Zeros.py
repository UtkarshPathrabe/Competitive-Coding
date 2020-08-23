class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        capacity = len(nums)
        while j < capacity:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        while i < capacity:
            nums[i] = 0
            i += 1