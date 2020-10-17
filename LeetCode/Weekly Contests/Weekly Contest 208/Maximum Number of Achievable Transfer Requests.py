class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegrees, numberOfRequests = defaultdict(int), len(requests)
        def backtrack(currentIndex):
            if currentIndex == numberOfRequests:
                for key, val in indegrees.items():
                    if val != 0:
                        return float('-inf')
                return 0
            source, destination = requests[currentIndex]
            indegrees[source] -= 1
            indegrees[destination] += 1
            result = 1 + backtrack(currentIndex + 1)
            indegrees[source] += 1
            indegrees[destination] -= 1
            return max(result, backtrack(currentIndex + 1))
        return backtrack(0)