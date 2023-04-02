class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]
        result = []
        def DFS(N, num):
            if N == 0:
                result.append(num)
            else:
                tailDigit = num % 10
                nextDigits = set([tailDigit + K, tailDigit - K])
                for nextDigit in nextDigits:
                    if nextDigit >= 0 and nextDigit < 10:
                        nextNumber = num * 10 + nextDigit
                        DFS(N - 1, nextNumber)
        for i in range(1, 10):
            DFS(N - 1, i)
        return result