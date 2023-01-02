class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result, numsCapacity = [], len(nums)
        def backtrack(currentCombination, counter):
            if numsCapacity == len(currentCombination):
                result.append(list(currentCombination))
                return
            for num in counter:
                if counter[num] > 0:
                    currentCombination.append(num)
                    counter[num] -= 1
                    backtrack(currentCombination, counter)
                    currentCombination.pop()
                    counter[num] += 1
        backtrack([], Counter(nums))
        return result