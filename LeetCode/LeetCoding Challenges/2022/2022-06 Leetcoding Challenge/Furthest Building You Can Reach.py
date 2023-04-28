class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladderAllocations = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heapq.heappush(ladderAllocations, climb)
            if len(ladderAllocations) <= ladders:
                continue
            bricks -= heapq.heappop(ladderAllocations)
            if bricks < 0:
                return i
        return len(heights) - 1