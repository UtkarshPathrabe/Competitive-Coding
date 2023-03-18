class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [char for char in str(num)]
        currentMax = num
        for i, digit in enumerate(nums):
            if digit == '6':
                currentMax = max(currentMax, int(''.join(nums[:i] + ['9'] + nums[i+1:])))
            else:
                currentMax = max(currentMax, int(''.join(nums[:i] + ['6'] + nums[i+1:])))
        return currentMax