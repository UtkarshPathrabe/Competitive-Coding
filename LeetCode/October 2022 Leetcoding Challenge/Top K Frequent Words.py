class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqMap = Counter(words)
        heap = [(-1 * freq, word) for word, freq in freqMap.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]