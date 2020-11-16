class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        
        def twoSumSmaller(startIndex, currentTarget):
            nonlocal result
            left, right = startIndex, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < currentTarget:
                    result += right - left
                    left += 1
                else:
                    right -= 1
        
        for i in range(len(nums) - 2):
            twoSumSmaller(i + 1, target - nums[i])
        return result