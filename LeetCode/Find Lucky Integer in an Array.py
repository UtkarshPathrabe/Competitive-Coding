class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        for key, val in sorted(counter.items(), reverse = True):
            if key == val:
                return key
        return -1