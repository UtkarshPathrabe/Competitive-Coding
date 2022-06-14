class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result, freqMap = 0, defaultdict(int)
        for num in nums:
            if freqMap[k - num] > 0:
                result += 1
                freqMap[k - num] -= 1
            else:
                freqMap[num] += 1
        return result