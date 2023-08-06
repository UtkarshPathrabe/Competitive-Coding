class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Add the first k workers with section id of 0 and 
        # the last k workers with section id of 1 (without duplication) to pq.
        pq = []
        for i in range(candidates):
            pq.append((costs[i], 0))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            pq.append((costs[i], 1))
        heapify(pq)
        result, nextHead, nextTail = 0, candidates, len(costs) - 1 - candidates
        # Only refill pq if there are workers outside.
        for _ in range(k):
            curCost, curSectionId = heappop(pq)
            result += curCost
            if nextHead <= nextTail:
                if curSectionId == 0:
                    heappush(pq, (costs[nextHead], 0))
                    nextHead += 1
                else:
                    heappush(pq, (costs[nextTail], 1))
                    nextTail -= 1
        return result