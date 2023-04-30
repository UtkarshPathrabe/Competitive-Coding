class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        @lru_cache(None)
        # dp(i, k): returns minimum difficulty when you start working on i-th job at day k
        def dp(i, k):
            # base case:
            # on the last day return maximum difficulty from all the remaining jobs
            if k == d:
                return max(jobDifficulty[i:])
            # initialize minimum difficulty with infinity
            result = float('inf')
            # initialize current maximum difficulty with 0
            currentMax = 0
            # for jobDifficulty like 6 5 4 3 2 1, 
            # we can have following ways to distribute them into two days
            # 6 | 5 4 3 2 1
            # 6 5 | 4 3 2 1 
            # 6 5 4 | 3 2 1
            # 6 5 4 3 | 2 1
            # 6 5 4 3 2 | 1
            # notice that each day we must have at least one task
            # given the starting index `i`, 
            # we can only at most choose the jobs till the position `n - (d - k) - 1`
            for j in range(i, n - (d - k)):
                currentMax = max(currentMax, jobDifficulty[j])
                # if j-th job is the last job on day `k`, 
                # the max difficulty for day `k` is `currentMax`
                # and we need to start (j + 1)-th job on the next day
                # the result would be `currentMax + dp(j + 1, k + 1)`
                # then we take the min
                result = min(result, currentMax + dp(j + 1, k + 1))
            return result
        # n < d : you will have free days. hence you cannot find a schedule for the given jobs
        # otherwise, we start working on 0-th job at day 1
        return -1 if n < d else dp(0, 1)