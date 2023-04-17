class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        dequeue, extraSlots, result = deque([]), len(nums) - k, [0] * k
        for num in nums:
            while len(dequeue) > 0 and dequeue[-1] > num and extraSlots > 0:
                dequeue.pop()
                extraSlots -= 1
            dequeue.append(num)
        for i in range(k):
            result[i] = dequeue.popleft()
        return result