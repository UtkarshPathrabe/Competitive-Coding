class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        stringLength = len(s)
        if stringLength < 3:
            return stringLength
        start, end = 0, 0
        characterMap = defaultdict()
        maxSubstringLength = 2
        while end < stringLength:
            if len(characterMap) < 3:
                characterMap[s[end]] = end
                end += 1
            if len(characterMap) == 3:
                deletionIndex = min(characterMap.values())
                del characterMap[s[deletionIndex]]
                start = deletionIndex + 1
            maxSubstringLength = max(maxSubstringLength, end - start)
        return maxSubstringLength