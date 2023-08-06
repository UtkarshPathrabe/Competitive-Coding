class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary, maxSalary, sumSalary = float('inf'), float('-inf'), 0
        for s in salary:
            sumSalary += s
            minSalary = min(minSalary, s)
            maxSalary = max(maxSalary, s)
        sumSalary -= (minSalary + maxSalary)
        return sumSalary / (len(salary) - 2)