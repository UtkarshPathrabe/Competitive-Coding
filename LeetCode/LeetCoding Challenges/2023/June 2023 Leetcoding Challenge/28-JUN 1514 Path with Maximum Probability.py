class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        maxProb = [0.0] * n
        maxProb[start] = 1.0
        pq = [(-1.0, start)]
        while pq:
            curProb, curNode = heapq.heappop(pq)
            if curNode == end:
                return -curProb
            for nextNode, pathProb in graph[curNode]:
                if -curProb * pathProb > maxProb[nextNode]:
                    maxProb[nextNode] = -curProb * pathProb
                    heapq.heappush(pq, (-maxProb[nextNode], nextNode))
        return 0.0