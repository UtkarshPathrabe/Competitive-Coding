class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentAltitude, maxAltitude = 0, 0
        for g in gain:
            currentAltitude += g
            maxAltitude = max(maxAltitude, currentAltitude)
        return maxAltitude