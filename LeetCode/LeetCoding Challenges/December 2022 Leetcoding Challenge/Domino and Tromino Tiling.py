class Solution:
    def numTilings(self, n: int) -> int:
        MOD = (10**9) + 7

        @cache
        def numTilingsD(N):
            if N <= 2:
                return 2 if N == 2 else 1
            return (numTilingsD(N - 2) + numTilingsD(N - 1) + (2 * numTilingsT(N - 1))) % MOD
        
        @cache
        def numTilingsT(N):
            if N <= 2:
                return 1 if N == 2 else 0
            return (numTilingsD(N - 2) + numTilingsT(N - 1)) % MOD
        
        return numTilingsD(n)