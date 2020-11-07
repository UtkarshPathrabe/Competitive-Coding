class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n, zippedList, bestScore = len(scores), sorted(zip(ages, scores)), 1
        dp = [c[1] for c in zippedList]
        for i in range(1, n):
            for j in range(i):
                if zippedList[i][1] >= zippedList[j][1]:
                    dp[i] = max(dp[i], dp[j] + zippedList[i][1])
                bestScore = max(bestScore, dp[i])
        return bestScore