class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        T = sum(calories[:k])
        def evaluate(T):
            if T < lower:
                return -1
            elif T > upper:
                return 1
            else:
                return 0
        points = evaluate(T)
        for i in range(k, len(calories)):
            T += (calories[i] - calories[i - k])
            points += evaluate(T)
        return points