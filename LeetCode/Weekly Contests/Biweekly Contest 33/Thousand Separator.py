class Solution:
    def thousandSeparator(self, n: int) -> str:
        return '.'.join(f'{n:,}'.split(','))