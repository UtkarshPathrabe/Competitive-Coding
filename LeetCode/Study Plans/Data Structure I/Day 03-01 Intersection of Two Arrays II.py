class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1FreqMap = Counter(nums1) # nums1 has smaller length
        result = []
        for num in nums2:
            if num in nums1FreqMap and nums1FreqMap[num] > 0:
                nums1FreqMap[num] -= 1
                result.append(num)
        return result