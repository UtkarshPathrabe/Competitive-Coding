class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        hashSet1, hashSet2, hashSet3 = set(nums1), set(nums2), set(nums3)
        freqMap = Counter(hashSet1) + Counter(hashSet2) + Counter(hashSet3)
        return [num for num, freq in freqMap.items() if freq > 1]