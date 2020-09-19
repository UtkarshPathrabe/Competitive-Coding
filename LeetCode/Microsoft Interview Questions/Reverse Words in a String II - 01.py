class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)
        helper(0, len(s) - 1)
        start = 0
        for end, char in enumerate(s):
            if char == ' ':
                helper(start, end - 1)
                start = end + 1
            if end == len(s) - 1:
                helper(start, end)