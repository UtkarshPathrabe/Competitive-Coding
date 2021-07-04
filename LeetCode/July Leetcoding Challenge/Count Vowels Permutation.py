# a => e + i + u
# e => a + i
# i => e + o
# o => i
# u => i + o

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD, curr = 1000000007, [1] * 5
        for i in range(2, n + 1):
            curr[0], curr[1], curr[2], curr[3], curr[4] = (curr[1] + curr[2] + curr[4]) % MOD, (curr[0] + curr[2]) % MOD, (curr[1] + curr[3]) % MOD, (curr[2]) % MOD, (curr[2] + curr[3]) % MOD
        return sum(curr) % MOD