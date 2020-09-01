class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1Map = {}
        for i, l in enumerate(list1):
            list1Map[l] = i
        result = []
        minimumSum = sys.maxsize
        i = 0
        while i < len(list2) and i <= minimumSum:
            if list2[i] in list1Map:
                currentSum = i + list1Map[list2[i]]
                if currentSum < minimumSum:
                    result = []
                    result.append(list2[i])
                    minimumSum = currentSum
                elif currentSum == minimumSum:
                    result.append(list2[i])
            i += 1
        return result