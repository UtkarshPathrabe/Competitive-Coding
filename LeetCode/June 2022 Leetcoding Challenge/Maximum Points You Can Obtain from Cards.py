class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        frontScore, rearScore, n = 0, 0, len(cardPoints)
        for i in range(k):
            frontScore += cardPoints[i]
        maxScore = frontScore
        for i in range(k - 1, -1, -1):
            rearScore += cardPoints[n - (k - i)]
            frontScore -= cardPoints[i]
            maxScore = max(maxScore, rearScore + frontScore)
        return maxScore