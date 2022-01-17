class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(list(zip(startTime, endTime, profit)))
        sortedStartedTime, N = [data[0] for data in jobs], len(jobs)
        dp = [0] * (N + 1)
        for k in range(N - 1, -1, -1):
            index = bisect.bisect_left(sortedStartedTime, jobs[k][1])
            dp[k] = max(jobs[k][2] + dp[index], dp[k + 1])
        return dp[0]