class ATM:

    def __init__(self):
        self.denominations, self.value = [0] * 5, {0: 20, 1: 50, 2: 100, 3: 200, 4: 500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for index, count in enumerate(banknotesCount):
            self.denominations[index] += count

    def withdraw(self, amount: int) -> List[int]:
        result = [0] * 5
        for index in range(4, -1, -1):
            requiredCount = min(amount // self.value[index], self.denominations[index])
            result[index] += requiredCount
            amount -= (requiredCount * self.value[index])
        if amount == 0:
            for index in range(5):
                self.denominations[index] -= result[index]
            return result
        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)