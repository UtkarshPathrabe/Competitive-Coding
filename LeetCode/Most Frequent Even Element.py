class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        heap = []
        for num, freq in freqMap.items():
            if num % 2 == 0:
                heapq.heappush(heap, (-freq, num))
        return heapq.heappop(heap)[1] if len(heap) > 0 else -1