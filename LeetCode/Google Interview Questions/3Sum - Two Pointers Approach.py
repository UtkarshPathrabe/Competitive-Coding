class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def twoSums(nums, i):
            nonlocal result
            low = i + 1
            high = len(nums) - 1
            while low < high:
                currentSum = nums[i] + nums[low] + nums[high]
                if currentSum > 0:
                    high -= 1
                elif currentSum < 0:
                    low += 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low - 1] == nums[low]:
                        low += 1
                
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i == 0 or nums[i - 1] != num:
                twoSums(nums, i)
        return result
    