class Solution:
    def isPalindrome(self, s: str) -> bool:
        formattedString = ''.join([c.lower() for c in s if c.isalnum()])
        if formattedString == formattedString[::-1]:
            return True
        return False