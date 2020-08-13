class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        result = [0] * numsLength
        for i in range(numsLength):
            smallerNumbers = result[i]
            for j in range(numsLength):
                if i != j and nums[j] < nums[i]:
                    smallerNumbers += 1
            result[i] = smallerNumbers
        return result