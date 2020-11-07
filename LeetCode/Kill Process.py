class Solution:
    def killProcess(self, pidList: List[int], ppidList: List[int], kill: int) -> List[int]:
        graph, visited = defaultdict(set), set()
        for pid, ppid in zip(pidList, ppidList):
            graph[ppid].add(pid)
        def dfs(i):
            visited.add(i)
            for pid in graph[i]:
                if pid not in visited:
                    dfs(pid)
        dfs(kill)
        return visited