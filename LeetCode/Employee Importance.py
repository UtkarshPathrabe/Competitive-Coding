"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], employeeId: int) -> int:
        subordinationGraph = defaultdict(list)
        importanceGraph = defaultdict(int)
        for employee in employees:
            subordinationGraph[employee.id].extend(employee.subordinates)
            importanceGraph[employee.id] = employee.importance
        if employeeId not in importanceGraph:
            return 0
        importance = importanceGraph[employeeId]
        
        def dfs(node):
            nonlocal importance
            for subordinate in subordinationGraph[node]:
                importance += importanceGraph[subordinate]
                dfs(subordinate)
        
        dfs(employeeId)
        return importance