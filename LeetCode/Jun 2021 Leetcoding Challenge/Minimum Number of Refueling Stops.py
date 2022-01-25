class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq, result, prev, tank = [], 0, 0, startFuel
        stations.append((target, float('inf')))
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:
                tank += -heapq.heappop(pq)
                result += 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -capacity)
            prev = location
        return result