class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x = y = direction = 0
        for i in instructions:
            if i == 'R':
                direction = (direction + 1) % 4
            elif i == 'L':
                direction = (direction + 3) % 4
            else:
                x += DIRECTIONS[direction][0]
                y += DIRECTIONS[direction][1]
        return (x == 0 and y == 0) or direction != 0