class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        poisonedDuration = 0
        for i in range(1, len(timeSeries)):
            poisonedDuration += min(timeSeries[i] - timeSeries[i - 1], duration)
        return poisonedDuration + duration