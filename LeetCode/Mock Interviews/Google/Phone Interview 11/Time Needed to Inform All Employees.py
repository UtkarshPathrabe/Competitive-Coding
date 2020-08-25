class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for index, managerId in enumerate(manager):
            graph[managerId].append(index)
        result = 0
        def dfs(node, currentTime):
            nonlocal graph, result
            if node not in graph:
                result = max(result, currentTime)
                return
            for emp in graph[node]:
                dfs(emp, currentTime + informTime[node])
        dfs(headID, 0)
        return result