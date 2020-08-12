class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0
        start = -1
        end = 0
        characterSet = set()
        stringLength = len(s)
        while start < stringLength and end < stringLength:
            currentChar = s[end]
            if currentChar in characterSet:
                start += 1
                characterToRemove = s[start]
                characterSet.remove(characterToRemove)
                longestSubstring = max(longestSubstring, end - start)
            else:
                characterSet.add(currentChar)
                longestSubstring = max(longestSubstring, end - start)
                end += 1
        return longestSubstring