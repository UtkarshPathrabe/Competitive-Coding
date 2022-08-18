class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freqMap = Counter(barcodes)
        heap = [(-freq, val) for val, freq in freqMap.items()]
        heapify(heap)
        index, result = 0, [0] * len(barcodes)
        while heap:
            freq, val = heappop(heap)
            for _ in range(-freq):
                result[index] = val
                index += 2
                if index >= len(barcodes):
                    index = 1
        return result