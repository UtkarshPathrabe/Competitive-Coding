class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        result, low, high = 0, 0, len(warehouse) - 1
        for box in sorted(boxes, reverse = True):
            if low <= high:
                if box <= warehouse[low]:
                    low, result = low + 1, result + 1
                elif box <= warehouse[high]:
                    high, result = high - 1, result + 1
        return result