class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        return s == ''.join(list(reversed(s)))