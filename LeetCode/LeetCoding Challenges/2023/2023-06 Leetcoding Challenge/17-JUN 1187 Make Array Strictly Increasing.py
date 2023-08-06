class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @lru_cache(None)
        def dfs(i: int, prev: int) -> int:
            if i == len(arr1):
                return 0
            cost = float('inf')
            # If arr1[i] is already greater than prev, we can leave it be.
            if arr1[i] > prev:
                cost = dfs(i + 1, arr1[i])
            # Find a replacement with the smallest value in arr2.
            index = bisect.bisect_right(arr2, prev)
            # Replace arr1[i], with a cost of 1 operation.
            if index < len(arr2):
                cost = min(cost, 1 + dfs(i + 1, arr2[index]))
            return cost
        
        result = dfs(0, -1)
        return result if result < float('inf') else -1