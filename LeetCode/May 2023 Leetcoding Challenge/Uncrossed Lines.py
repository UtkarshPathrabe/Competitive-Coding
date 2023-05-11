class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        
        @lru_cache(None)
        def helper(n1: int, n2: int):
            if n1 <= 0 or n2 <= 0:
                return 0
            if nums1[n1 - 1] == nums2[n2 - 1]:
                return 1 + helper(n1 - 1, n2 - 1)
            else:
                return max(helper(n1 - 1, n2), helper(n1, n2 - 1))
        
        return helper(len1, len2)