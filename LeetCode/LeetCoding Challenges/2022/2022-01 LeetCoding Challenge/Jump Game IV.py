class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        graph = defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)
        queue, visited, steps = deque([(0, 0)]), set([0]), 0
        while queue:
            node, depth = queue.popleft()
            if node == len(arr) - 1:
                return depth
            for neighbour in graph[arr[node]]:
                if neighbour not in visited:
                    queue.append((neighbour, depth + 1))
                    visited.add(neighbour)
            graph[arr[node]].clear()
            for neighbour in [node - 1, node + 1]:
                if 0 <= neighbour < len(arr) and neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, depth + 1))
        return -1