class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, duplicates, seen = set(), set(), {}
        for i, num1 in enumerate(nums):
            if num1 not in duplicates:
                duplicates.add(num1)
                for j, num2 in enumerate(nums[i + 1:]):
                    complement = -num1 - num2
                    if complement in seen and seen[complement] == i:
                        result.add(tuple(sorted((num1, num2, complement))))
                    seen[num2] = i
        return result