class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPalindrome(s):
            low, high = 0, len(s) - 1
            while low < high:
                if s[low] != s[high]:
                    return False
                low, high = low + 1, high - 1
            return True
        if not s:
            return 0
        if isPalindrome(s):
            return 1
        return 2