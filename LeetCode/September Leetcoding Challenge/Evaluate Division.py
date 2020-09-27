class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict()
        for index, (source, destination) in enumerate(equations):
            if source not in graph:
                graph[source] = defaultdict(int)
            graph[source][destination] = float(values[index])
            if destination not in graph:
                graph[destination] = defaultdict(int)
            graph[destination][source] = float(1 / values[index])
        def dfs(source, destination, currentValue, visitedSet):
            nonlocal graph
            if source in visitedSet:
                return
            visitedSet.add(source)
            if source == destination:
                self.currentResult = currentValue
                return
            for neighbour, value in graph[source].items():
                dfs(neighbour, destination, currentValue * value, visitedSet)
        result = []
        for source, destination in queries:
            if source not in graph or destination not in graph:
                result.append(-1.0)
            elif source == destination:
                result.append(1.0)
            elif destination in graph[source]:
                result.append(graph[source][destination])
            else:
                self.currentResult = -1.0
                dfs(source, destination, 1.0, set())
                result.append(self.currentResult)
        return result