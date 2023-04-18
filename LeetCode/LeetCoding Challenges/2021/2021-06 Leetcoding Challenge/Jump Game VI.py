class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score, dequeue = [0] * n, deque([0,])
        score[0] = nums[0]
        for i in range(1, n):
            while dequeue and dequeue[0] < i - k:
                dequeue.popleft()
            score[i] = nums[i] + score[dequeue[0]]
            while dequeue and score[dequeue[-1]] <= score[i]:
                dequeue.pop()
            dequeue.append(i)
        return score[-1]