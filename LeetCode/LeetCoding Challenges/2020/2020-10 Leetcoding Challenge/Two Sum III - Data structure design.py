class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.countMap = defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.countMap[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.countMap.keys():
            complement = value - num
            if complement == num:
                if self.countMap[num] > 1:
                    return True
            else:
                if complement in self.countMap:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)