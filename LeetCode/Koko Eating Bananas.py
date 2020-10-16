class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(k):
            return sum(math.ceil(p / k) for p in piles) <= H
        low, high = 1, max(piles)
        while low < high:
            mid = low + (high - low) // 2
            if not possible(mid):
                low = mid + 1
            else:
                high = mid
        return low