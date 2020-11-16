class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        getScore = lambda i, j : (A[i] + A[j] + i - j)
        a, b = 0, 1
        dp = [A[0], getScore(0, 1)] + [0 for _ in range(2, len(A))]
        maxScore = max(dp[0], dp[1])
        for i in range(2, len(A)):
            scorea, scoreb = getScore(a, i), getScore(b, i)
            if scorea > scoreb:
                dp[i] = scorea
                b = i
            else:
                dp[i] = scoreb
                a, b = b, i
            maxScore = max(maxScore, dp[i])
        return maxScore