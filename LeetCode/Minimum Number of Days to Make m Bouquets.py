class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left, right = 0, max(bloomDay)
        while left < right:
            mid = (left + right) >> 1
            flowers = bouquets = 0
            for bloom in bloomDay:
                flowers = 0 if bloom > mid else flowers + 1
                if flowers >= k:
                    flowers, bouquets = 0, bouquets + 1
                    if bouquets == m:
                        break
            if bouquets == m:
                right = mid
            else:
                left = mid + 1
        return left