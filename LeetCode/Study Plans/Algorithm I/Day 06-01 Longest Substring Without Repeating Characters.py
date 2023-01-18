class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindow = 0
        start = end = 0
        alphabets = set()
        while( end < len(s) ):
            if( s[end] not in alphabets ):
                alphabets.add(s[end])
                end += 1
                maxWindow = max( maxWindow, end - start )
            else:
                alphabets.remove(s[start])
                start += 1
        return maxWindow