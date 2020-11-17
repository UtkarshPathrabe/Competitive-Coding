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
        maxWeight, low, high = max(weights), sum(weights) // D, max(weights) * len(weights) // D + 1
        while low < high:
            mid = low + ((high - low) >> 1)
            if mid < maxWeight or not possible(mid):
                low = mid + 1
            else:
                high = mid
        return low