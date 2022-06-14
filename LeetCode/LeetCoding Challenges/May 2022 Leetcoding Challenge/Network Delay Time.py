class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for From, To, Time in times:
            graph[From].append((To, Time))
        heap = [(0, K)]
        times = {}
        while heap:
            time, node = heappop(heap)
            if node not in times:
                times[node] = time
                for neighbour, Time in graph[node]:
                    if neighbour not in times:
                        heappush(heap, (time + Time, neighbour))
        return max(times.values()) if len(times) == N else -1