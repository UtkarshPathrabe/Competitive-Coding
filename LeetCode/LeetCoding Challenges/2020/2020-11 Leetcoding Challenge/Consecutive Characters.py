class Solution:
    def maxPower(self, s: str) -> int:
        power, maxPow = 1, 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                power += 1
            else:
                maxPow = max(maxPow, power)
                power = 1
        return max(maxPow, power)