class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        dp = [0] * n
        for i, j, k in bookings:
            dp[i - 1] += k
            if j < n:
                dp[j] -= k
        result = [0] * n
        result[0] = dp[0]
        for i in range(1, n):
            result[i] = result[i - 1] + dp[i]
        return result