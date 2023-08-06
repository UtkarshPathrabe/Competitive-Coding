class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n, MOD, result = len(nums), 10 ** 9 + 7, 0
        nums.sort()
        for left in range(n):
            # Find the insertion position for `target - nums[left]`
            # 'right' equals the insertion index minus 1.
            right = bisect.bisect_right(nums, target - nums[left]) - 1
            if right >= left:
                result += pow(2, right - left, MOD)
        return result % MOD