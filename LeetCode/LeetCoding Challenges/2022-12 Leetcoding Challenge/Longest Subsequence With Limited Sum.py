class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefixSum = sorted(nums)
        for i in range(1, len(nums)):
            prefixSum[i] += prefixSum[i - 1]
        result = []
        for query in queries:
            index = bisect.bisect_right(prefixSum, query)
            result.append(index)
        return result