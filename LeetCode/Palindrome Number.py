class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        reverseNumber = 0
        while x > reverseNumber:
            reverseNumber = reverseNumber * 10 + x % 10
            x = x // 10
        return x == reverseNumber or x == reverseNumber // 10