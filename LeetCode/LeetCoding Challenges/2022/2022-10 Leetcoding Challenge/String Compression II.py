class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(currentIndex, prevChar, prevCharCount, charsToDelete):
            # if chars to delete is less than 0, then return inf as this is impossible
            if charsToDelete < 0:
                return float('inf')
            # if current index is greater than or equal to input string len then return 0 as we have traversed the full string and this is the base case
            if currentIndex >= len(s):
                return 0
    
            # two choices, 1. delete the current character, 2. keep the current character
            # calculate both results and take the minimum one
            
            # delete the current character
            charDeletionLen = dp(currentIndex + 1, prevChar, prevCharCount, charsToDelete - 1)
    
            if s[currentIndex] == prevChar:
                # e.g. a2 -> a3, a7 -> a8
                charKeepLen = dp(currentIndex + 1, prevChar, prevCharCount + 1, charsToDelete)
                # add an extra character to run length encoding when current character count is either 1, 9 or 99
                # e.g. a -> a2, a9 -> a10, a99 -> a100
                if prevCharCount in [1, 9, 99]:
                    charKeepLen += 1
            else:
                # a new character was found, increase the length by 1 plus the cost of compressing the rest of the string
                # e.g. b
                charKeepLen = 1 + dp(currentIndex + 1, s[currentIndex], 1, charsToDelete)
            return min(charKeepLen, charDeletionLen)
    
        return dp(0, "", 0, k)