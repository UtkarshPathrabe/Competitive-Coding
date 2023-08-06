class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]

        @lru_cache(None)
        def cost(left: int, right: int) -> int:
            if right - left == 1:
                return 0
            return min(cost(left, mid) + cost(mid, right) + cuts[right] - cuts[left] for mid in range(left + 1, right))
        
        return cost(0, len(cuts) - 1)