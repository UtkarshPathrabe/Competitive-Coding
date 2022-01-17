# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        row, col = rand7(), rand7()
        index = col + (row - 1) * 7
        while index > 40:
            row, col = rand7(), rand7()
            index = col + (row - 1) * 7
        return 1 + (index - 1) % 10