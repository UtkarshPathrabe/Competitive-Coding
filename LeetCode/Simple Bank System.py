class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.numberofAccounts = len(balance)
    
    def _isAccountNumberValid(self, account: int) -> bool:
        return 1 <= account <= self.numberofAccounts
    
    def _canProceedWithWithdrawal(self, account: int, money: int) -> bool:
        return self._isAccountNumberValid(account) and self.balance[account - 1] >= money

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._canProceedWithWithdrawal(account1, money) and self._isAccountNumberValid(account2):
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self._isAccountNumberValid(account):
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self._canProceedWithWithdrawal(account, money):
            self.balance[account - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)