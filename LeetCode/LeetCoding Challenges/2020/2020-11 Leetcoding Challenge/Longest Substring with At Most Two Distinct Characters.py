class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        start, end, maxSubstringLength, lastCharIndexMap = 0, 0, 2, defaultdict(int)
        while end < len(s):
            if len(lastCharIndexMap) < 3:
                lastCharIndexMap[s[end]] = end
                end += 1
            if len(lastCharIndexMap) == 3:
                minIndex = min(lastCharIndexMap.values())
                del lastCharIndexMap[s[minIndex]]
                start = minIndex + 1
            maxSubstringLength = max(maxSubstringLength, end - start)
        return maxSubstringLength