class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        def kSum(nums, target, k):
            result, numsLen = [], len(nums)
            if numsLen == 0 or nums[0] * k > target or nums[-1] * k < target:
                return result
            if k == 2:
                return twoSum(nums, target)
            for i in range(numsLen):
                if i == 0 or nums[i - 1] != nums[i]:
                    for resultSubset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        result.append([nums[i]] + resultSubset)
            return result
        
        def twoSum(nums, target):
            result, numsLen = [], len(nums)
            left, right = 0, numsLen - 1
            while left < right:
                currentSum = nums[left] + nums[right]
                if currentSum < target or (left > 0 and nums[left - 1] == nums[left]):
                    left += 1
                elif currentSum > target or (right < numsLen - 1 and nums[right] == nums[right + 1]):
                    right -= 1
                else:
                    result.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
            return result
        
        return kSum(nums, target, 4)