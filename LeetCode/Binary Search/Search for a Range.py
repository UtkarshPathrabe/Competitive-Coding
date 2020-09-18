class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def indexSearch(nums, target, left):
            low = 0
            high = len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] > target or (left and target == nums[mid]):
                    high = mid
                else:
                    low = mid + 1
            return low
        
        leftIndex = indexSearch(nums, target, True)
        if leftIndex == len(nums) or nums[leftIndex] != target:
            return [-1, -1]
        else:
            return [leftIndex, indexSearch(nums, target, False) - 1]