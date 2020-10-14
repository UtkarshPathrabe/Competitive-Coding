class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count = [0] * len(nums)
        for start, end in requests:
            count[start] += 1
            if end + 1 < len(count):
                count[end + 1] -= 1
        currentCount = 0
        for i in range(len(count)):
            count[i] += currentCount
            currentCount = count[i]
        return sum(num * freq for num, freq in zip(sorted(nums, reverse = True), sorted(count, reverse = True))) % (10 ** 9 + 7)