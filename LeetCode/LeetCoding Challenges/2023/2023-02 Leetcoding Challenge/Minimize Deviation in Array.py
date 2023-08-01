class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        evens, minimum, minDeviation = [], float('inf'), float('inf')
        for num in nums:
            if num % 2 == 0:
                evens.append(-num)
                minimum = min(minimum, num)
            else:
                evens.append(-num * 2)
                minimum = min(minimum, num * 2)
        heapify(evens)
        while evens:
            val = -heappop(evens)
            minDeviation = min(minDeviation, val - minimum)
            if val % 2 == 0:
                minimum = min(minimum, val // 2)
                heappush(evens, -val // 2)
            else:
                break
        return minDeviation