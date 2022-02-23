class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def helper(low, high, k):
            if low == high:
                return 0
            while low + 1 < high and boxes[low] == boxes[low + 1]:
                low, k = low + 1, k + 1
            result = (k + 1) * (k + 1) + helper(low + 1, high, 0)
            for mid in range(low + 2, high):
                if boxes[low] == boxes[mid]:
                    result = max(result, helper(low + 1, mid, 0) + helper(mid, high, k + 1))
            return result
        return helper(0, len(boxes), 0)