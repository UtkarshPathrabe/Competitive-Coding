class Solution:
    def largestVariance(self, s: str) -> int:
        counter = [0] * 26
        for char in s:
            counter[ord(char) - ord('a')] += 1
        globalMax = 0
        for i in range(26):
            for j in range(26):
                # major and minor cannot be the same, and both must appear in s.
                if i == j or counter[i] == 0 or counter[j] == 0:
                    continue
                # find the maximum variance of major - minor
                major = chr(ord('a') + i)
                minor = chr(ord('a') + j)
                majorCount, minorCount = 0, 0
                # The remaining minor in the rest of s
                restMinor = counter[j]
                for char in s:
                    if char == major:
                        majorCount += 1
                    if char == minor:
                        minorCount += 1
                        restMinor -= 1
                    # Only update the variance if there is at least one minor
                    if minorCount > 0:
                        globalMax = max(globalMax, majorCount - minorCount)
                    # We can discard the previous string if there is at least one remaining minor
                    if majorCount < minorCount and restMinor > 0:
                        majorCount, minorCount = 0, 0
        return globalMax