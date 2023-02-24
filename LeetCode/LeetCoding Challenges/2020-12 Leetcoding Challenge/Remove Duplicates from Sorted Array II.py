class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, currentElementCount = 0, 1
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                currentElementCount = 1
            elif nums[i] == nums[j] and currentElementCount < 2:
                i += 1
                nums[i] = nums[j]
                currentElementCount += 1
        return i + 1