class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourAngle = ((hour % 12) + (minutes / 60)) * 30
        minuteAngle = (minutes % 60) * 6
        diff = abs(hourAngle - minuteAngle)
        return min(diff, 360 - diff)