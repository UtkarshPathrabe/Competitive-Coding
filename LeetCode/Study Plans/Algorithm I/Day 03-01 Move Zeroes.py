class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, N = 0, 0, len(nums)
        while j < N:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        while i < N:
            nums[i] = 0
            i += 1