class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowestKey, maximumTime = keysPressed[0], releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            keyPressTime = releaseTimes[i] - releaseTimes[i - 1]
            if keyPressTime > maximumTime or (keyPressTime == maximumTime and keysPressed[i] > slowestKey):
                maximumTime = keyPressTime
                slowestKey = keysPressed[i]
        return slowestKey