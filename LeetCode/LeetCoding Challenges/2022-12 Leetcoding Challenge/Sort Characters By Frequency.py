class Solution:
    def frequencySort(self, s: str) -> str:
        freqMap = Counter(s)
        heap, result = [], []
        for char, freq in freqMap.items():
            heapq.heappush(heap, (-freq, char))
        while heap:
            freq, char = heapq.heappop(heap)
            result.extend(char * -freq)
        return ''.join(result)