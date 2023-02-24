class strNumComp(str):
    
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sortedNums = ''.join(sorted(map(str, nums), key = strNumComp))
        return '0' if sortedNums[0] == '0' else sortedNums