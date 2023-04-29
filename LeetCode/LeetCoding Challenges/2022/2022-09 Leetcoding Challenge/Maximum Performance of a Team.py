class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MODULO = 10 ** 9 + 7
        # build tuples of (efficiency, speed)
        candidates = zip(efficiency, speed)
        # sort the candidates by their efficiencies
        candidates = sorted(candidates, key=lambda t:t[0], reverse=True)
        speedHeap, speedSum, performance = [], 0, 0
        for currEfficiency, currSpeed in candidates:
            # maintain a heap for the fastest (k-1) speeds
            if len(speedHeap) > k-1:
                speedSum -= heapq.heappop(speedHeap)
            heapq.heappush(speedHeap, currSpeed)
            # calculate the maximum performance with the current member as the least efficient one in the team
            speedSum += currSpeed
            performance = max(performance, speedSum * currEfficiency)
        return performance % MODULO