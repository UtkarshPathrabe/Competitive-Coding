class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from sortedcontainers import SortedDict
        count, size = SortedDict(Counter(nums)), len(nums)
        i = size - 2 if size % 2 == 0 else size - 1
        for key, value in count.items():
            for j in range(value):
                nums[i] = key
                i -= 2
                if i < 0:
                    i = size - 2 if size % 2 != 0 else size - 1