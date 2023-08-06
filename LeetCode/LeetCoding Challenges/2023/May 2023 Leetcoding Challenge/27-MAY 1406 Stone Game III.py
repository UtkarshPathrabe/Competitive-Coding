class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def helper(i: int) -> int:
            if i == n:
                return 0
            result = stoneValue[i] - helper(i + 1)
            if i + 2 <= n:
                result = max(result, stoneValue[i] + stoneValue[i + 1] - helper(i + 2))
            if i + 3 <= n:
                result = max(result, stoneValue[i] + stoneValue[i + 1] + stoneValue[ i + 2] - helper(i + 3))
            return result
        
        result = helper(0)
        if result > 0:
            return 'Alice'
        elif result < 0:
            return 'Bob'
        else:
            return 'Tie'