class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, remainder = divmod(sum(nums), k)
        if remainder or max(nums) > target:
            return False
        dp = [None] * (1 << len(nums))
        dp[-1] = True
        def search(used, todo):
            if dp[used] is None:
                tar = (todo - 1) % target + 1
                dp[used] = any(search(used | (1 << i), todo - num) for i, num in enumerate(nums) if (used >> i) & 1 == 0 and num <= tar)
            return dp[used]
        return search(0, target * k)