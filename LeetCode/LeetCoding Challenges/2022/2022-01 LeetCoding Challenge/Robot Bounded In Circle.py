class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x = y = dir = 0
        for char in instructions:
            if char == 'L':
                dir = (dir + 1) % 4
            elif char == 'R':
                dir = (dir - 1) % 4
            else:
                x, y = x + DIR[dir][0], y + DIR[dir][1]
        return x == 0 and y == 0 or dir > 0
# Robot will move in circle if the end direction is not North or it is at origin