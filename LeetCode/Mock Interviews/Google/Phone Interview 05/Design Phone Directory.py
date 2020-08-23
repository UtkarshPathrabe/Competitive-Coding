class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.numbers = {i for i in range(maxNumbers)}

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.numbers:
            return self.numbers.pop()
        return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.numbers

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.numbers.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)