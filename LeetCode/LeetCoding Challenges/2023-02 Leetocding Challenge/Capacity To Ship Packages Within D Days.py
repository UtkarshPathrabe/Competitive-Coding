class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def possible(capacity):
            count, loaded = 1, 0
            for w in weights:
                if loaded + w <= capacity:
                    loaded += w
                else:
                    count += 1
                    loaded = w
            return count <= D
        maxWeight, low, high = max(weights), max(weights), sum(weights)
        while low <= high:
            mid = (high + low) >> 1
            if mid < maxWeight or not possible(mid):
                low = mid + 1
            else:
                high = mid - 1
        return low