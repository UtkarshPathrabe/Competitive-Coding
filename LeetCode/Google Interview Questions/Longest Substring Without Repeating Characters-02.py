class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0
        characterMap = dict()
        stringLength = len(s)
        start, end = 0, 0
        while end < stringLength:
            if characterMap.get(s[end]):
                start = max(characterMap.get(s[end]), start)
            longestSubstring = max(longestSubstring, end - start + 1)
            characterMap[s[end]] = end + 1
            end += 1
        return longestSubstring