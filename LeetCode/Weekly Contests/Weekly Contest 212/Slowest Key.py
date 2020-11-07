class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxTime, maxTimeChar = releaseTimes[0], keysPressed[0]
        for i in range(1, len(releaseTimes)):
            releaseTime = releaseTimes[i] - releaseTimes[i - 1]
            if releaseTime > maxTime:
                maxTime, maxTimeChar = releaseTime, keysPressed[i]
            elif releaseTime == maxTime:
                if maxTimeChar < keysPressed[i]:
                    maxTimeChar = keysPressed[i]
        return maxTimeChar