class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        def permute(nums, currentIndex):
            nonlocal count
            if currentIndex == len(nums):
                count += 1
            for i in range(currentIndex, len(nums)):
                swap(nums, i, currentIndex)
                if nums[currentIndex] % (currentIndex + 1) == 0 or (currentIndex + 1) % nums[currentIndex] == 0:
                    permute(nums, currentIndex + 1)
                swap(nums, currentIndex, i)
        nums = [i + 1 for i in range(n)]
        permute(nums, 0)
        return count