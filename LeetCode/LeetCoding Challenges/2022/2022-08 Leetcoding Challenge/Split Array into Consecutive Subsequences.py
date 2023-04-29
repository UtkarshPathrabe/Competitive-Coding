class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        freqMap = Counter(nums)
        subsequence = defaultdict(int)
        for num in nums:
            if freqMap[num] == 0:
                continue
            freqMap[num] -= 1
            # option 1 - add to an existing subsequence
            if subsequence[num - 1] > 0:
                subsequence[num - 1] -= 1
                subsequence[num] += 1
            # option 2 - create a new subsequence
            elif freqMap[num + 1] and freqMap[num + 2]:
                subsequence[num + 2] += 1
                freqMap[num + 1] -= 1
                freqMap[num + 2] -= 1
            else:
                return False
        return True