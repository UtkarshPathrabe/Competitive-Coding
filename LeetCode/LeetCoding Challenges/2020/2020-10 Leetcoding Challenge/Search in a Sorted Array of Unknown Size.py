# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        left, right = 0, 1
        while reader.get(right) < target:
            left, right = right, right << 1
        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)
            if num == target:
                return pivot
            elif num < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1