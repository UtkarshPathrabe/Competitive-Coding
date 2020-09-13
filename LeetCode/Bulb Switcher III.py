class Solution:
    def numTimesAllBlue(self, lights: List[int]) -> int:
        result, maxLightOn = 0, 0
        for moment, light in enumerate(lights, 1):
            maxLightOn = max(maxLightOn, light)
            if maxLightOn == moment:
                result += 1
        return result