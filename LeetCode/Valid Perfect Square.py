class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num
        while left <= right:
            mid = left + ((right - left) >> 1)
            n = mid * mid
            if n == num:
                return True
            elif n > num:
                right = mid - 1
            else:
                left = mid + 1
        return False