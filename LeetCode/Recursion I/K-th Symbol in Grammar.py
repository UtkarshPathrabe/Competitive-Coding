class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return bin(K - 1).count('1') % 2