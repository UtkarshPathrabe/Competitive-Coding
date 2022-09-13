class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for i, num in enumerate(nums):
            if i % 2:
                odd.append(num)
            else:
                even.append(num)
        odd.sort(reverse=True)
        even.sort()
        result = [None] * len(nums)
        for i, num in enumerate(even):
            result[2 * i] = num
        for i, num in enumerate(odd):
            result[(2 * i) + 1] = num
        return result