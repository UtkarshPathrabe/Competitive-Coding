class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), math.ceil(sum(amount) / 2))