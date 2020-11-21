class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        start, end = 0, len(nums) - 1
        def isBinarySearchHelpful(start, element):
            return nums[start] != element
        def existsInFirst(start, element):
            return nums[start] <= element
        while start <= end:
            mid = start + ((end - start) >> 1)
            if nums[mid] == target:
                return True
            if not isBinarySearchHelpful(start, nums[mid]):
                start += 1
                continue
            pivotArray, targetArray = existsInFirst(start, nums[mid]), existsInFirst(start, target)
            if pivotArray ^ targetArray:
                if pivotArray:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return False