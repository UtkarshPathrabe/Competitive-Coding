class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = []
        for i in range(n - 1, -1, -1):
            toRemove = min(k - i, 26)
            result.append(chr(toRemove + ord('a') - 1))
            k -= toRemove
        return ''.join(result[::-1])