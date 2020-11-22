# a => e + i + u
# e => a + i
# i => e + o
# o => i
# u => i + o

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD, prev, curr = 1000000007, [1] * 5, [None] * 5
        for i in range(2, n + 1):
            curr[0] = (prev[1] + prev[2] + prev[4]) % MOD
            curr[1] = (prev[0] + prev[2]) % MOD
            curr[2] = (prev[1] + prev[3]) % MOD
            curr[3] = (prev[2]) % MOD
            curr[4] = (prev[2] + prev[3]) % MOD
            for i in range(5):
                prev[i] = curr[i]
        return sum(prev) % MOD