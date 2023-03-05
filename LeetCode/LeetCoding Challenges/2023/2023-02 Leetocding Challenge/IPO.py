class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        n = len(projects)
        projects.sort()
        heap, pointer = [], 0
        for i in range(k):
            while pointer < n and projects[pointer][0] <= w:
                heappush(heap, -projects[pointer][1])
                pointer += 1
            if not heap:
                break
            w += -heappop(heap)
        return w