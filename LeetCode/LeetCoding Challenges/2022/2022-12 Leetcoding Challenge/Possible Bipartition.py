class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])
        color = [-1 for _ in range(n + 1)]
        def bfs(src):
            queue = deque([src])
            color[src] = 0
            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if color[neighbour] == color[node]:
                        return False
                    if color[neighbour] == -1:
                        queue.append(neighbour)
                        color[neighbour] = 1 - color[node]
            return True
        for i in range(1, n+1):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True