class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R, MAGIC = int(left), int(right), 100000
        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x = x // 10
            return ans
        def isPalindrome(x):
            return x == reverse(x)
        result = 0
        for k in range(MAGIC):
            s = str(k)
            v = int(s + s[-2::-1]) ** 2
            if v > R:
                break
            if v >= L and isPalindrome(v):
                result += 1
        for k in range(MAGIC):
            s = str(k)
            v = int(s + s[::-1]) ** 2
            if v > R:
                break
            if v >= L and isPalindrome(v):
                result += 1
        return result