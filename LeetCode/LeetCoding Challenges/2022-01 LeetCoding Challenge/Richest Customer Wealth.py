class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(person) for person in accounts)