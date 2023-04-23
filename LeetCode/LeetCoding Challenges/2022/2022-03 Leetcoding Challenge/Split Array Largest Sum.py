class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        def isFeasible(threshold):
            total, count = 0, 1
            for num in nums:
                total += num
                if total > threshold:
                    count += 1
                    total = num
                    if count > m:
                        return False
            return True
        while left < right:
            mid = left + (right - left) // 2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        return left