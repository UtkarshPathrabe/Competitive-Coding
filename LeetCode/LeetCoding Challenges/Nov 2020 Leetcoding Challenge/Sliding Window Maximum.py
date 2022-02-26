class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) * k == 0:
            return []
        if k == 1:
            return nums
        dequeue, result, maxIndex = deque(), [], 0
        def cleanDeque(i):
            if dequeue and dequeue[0] == i - k:
                dequeue.popleft()
            while dequeue and nums[i] > nums[dequeue[-1]]:
                dequeue.pop()
        for i in range(k):
            cleanDeque(i)
            dequeue.append(i)
            if nums[i] > nums[maxIndex]:
                maxIndex = i
        result.append(nums[maxIndex])
        for i in range(k, len(nums)):
            cleanDeque(i)
            dequeue.append(i)
            result.append(nums[dequeue[0]])
        return result