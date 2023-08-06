class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)

        @lru_cache(None)
        def helper(i: int) -> int:
            if i > N - 1:
                return 0
            elif i == N - 1:
                return questions[i][0]
            else:
                return max(helper(i + 1), questions[i][0] + helper(i + questions[i][1] + 1))
        
        return helper(0)