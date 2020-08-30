class Solution:
    def rob(self, nums: List[int]) -> int:
        numsCapacity = len(nums)
        if numsCapacity == 0:
            return 0
        if numsCapacity == 1:
            return nums[0]
        def simpleRob(nums):
            t1, t2 = 0, 0
            for num in nums:
                t1, t2 = max(num + t2, t1), t1
            return t1
        return max(simpleRob(nums[:-1]), simpleRob(nums[1:]))