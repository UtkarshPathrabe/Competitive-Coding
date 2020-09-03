class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numberCount = defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.numberCount[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for number in self.numberCount.keys():
            complementNumber = value - number
            if complementNumber == number:
                if self.numberCount[number] > 1:
                    return True
            else:
                if complementNumber in self.numberCount:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)