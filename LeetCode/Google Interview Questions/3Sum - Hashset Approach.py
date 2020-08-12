class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def twoSums(nums, i):
            nonlocal result
            seenSet = set()
            j = i + 1
            while j < len(nums):
                complement = -nums[i] - nums[j]
                if complement in seenSet:
                    result.append([nums[i], complement, nums[j]])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seenSet.add(nums[j])
                j += 1
                
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i == 0 or nums[i - 1] != num:
                twoSums(nums, i)
        return result
    