class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        sLen, MOD = len(s), 10**9 + 7
        # Number of possible splits for s[start ~ sLen-1].
        @lru_cache(None)
        def dfs(start: int) -> int:
            # There is only 1 split for an empty string.
            if start == sLen:
                return 1
            # Number can't have leading zeros.
            if s[start] == '0':
                return 0
            # For all possible starting number, add the number of arrays 
            # that can be printed as the remaining string to currentCount.
            currentCount = 0
            for end in range(start, sLen):
                currentNumber = s[start: end + 1]
                if int(currentNumber) > k:
                    break
                currentCount += dfs(end + 1)
            return currentCount % MOD
        return dfs(0) % MOD