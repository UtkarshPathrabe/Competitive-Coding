class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums) - 2):
            if nums[i] != 0:
                k = i + 2
                for j in range(i + 1, len(nums) - 1):
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        k += 1
                    result += k - j - 1
        return result