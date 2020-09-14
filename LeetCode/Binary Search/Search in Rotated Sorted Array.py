class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            pivot = start + (end - start) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] >= nums[start]:
                if target >= nums[start] and target < nums[pivot]:
                    end = pivot - 1
                else:
                    start = pivot + 1
            else:
                if target > nums[pivot] and target <= nums[end]:
                    start = pivot + 1
                else:
                    end = pivot - 1
        return -1