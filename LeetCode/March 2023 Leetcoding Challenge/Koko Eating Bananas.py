class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            return sum(math.ceil(p / k) for p in piles) <= h
        low, high, result = 1, max(piles), max(piles)
        while low <= high:
            mid = low + ((high - low) >> 1)
            if not possible(mid):
                low = mid + 1
            else:
                result = mid
                high = mid - 1
        return result