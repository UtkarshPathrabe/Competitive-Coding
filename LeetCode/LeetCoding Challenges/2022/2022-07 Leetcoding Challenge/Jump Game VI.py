class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n, score, dq = len(nums), nums[0], deque([(0, nums[0]),])
        for i in range(1, n):
            while dq and dq[0][0] < i - k:
                dq.popleft()
            score = dq[0][1] + nums[i]
            while dq and score >= dq[-1][1]:
                dq.pop()
            dq.append((i, score))
        return score