class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0
        for i in range(k + 1):
            temp = dist[::]
            for flight in flights:
                if dist[flight[0]] != float('inf'):
                    temp[flight[1]] = min(temp[flight[1]], dist[flight[0]] + flight[2])
            dist = temp
        return -1 if dist[dst] == float('inf') else dist[dst]