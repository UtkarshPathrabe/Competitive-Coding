class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        numsMap = Counter(nums1)
        result = []
        for i, num in enumerate(nums2):
            if num in numsMap and numsMap[num] > 0:
                result.append(num)
                numsMap[num] -= 1
        return result