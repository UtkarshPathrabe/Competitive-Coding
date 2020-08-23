class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsCapacity = len(nums)
        for i in range(numsCapacity):
            newIndex = abs(nums[i]) - 1
            if nums[newIndex] > 0:
                nums[newIndex] *= -1
        result = []
        for i in range(1, numsCapacity + 1):
            if nums[i - 1] > 0:
                result.append(i)
        return result