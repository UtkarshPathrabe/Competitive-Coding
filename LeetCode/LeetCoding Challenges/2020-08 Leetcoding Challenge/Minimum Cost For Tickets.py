class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        durations = [1, 7, 30]
        
        @lru_cache(None)
        def dp(i):
            if i >= N:
                return 0
            result = float('inf')
            j = i
            for cost, duration in zip(costs, durations):
                while j < N and days[j] < days[i] + duration:
                    j += 1
                result = min(result, dp(j) + cost)
            return result
        
        return dp(0)