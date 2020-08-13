class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        result = [0] * numsLength
        newList = nums[:]
        newList.sort()
        for i, num in enumerate(nums):
            index = bisect_left(newList, num)
            result[i] = index
        return result