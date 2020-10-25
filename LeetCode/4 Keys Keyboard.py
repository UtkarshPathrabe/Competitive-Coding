class Solution:
    def maxA(self, N: int) -> int:
        best = [0, 1]
        for k in range(2, N + 1):
            best.append(max(best[x] * (k - x - 1) for x in range(k - 1)))
            best[-1] = max(best[-1], best[-2] + 1)
        return best[N]