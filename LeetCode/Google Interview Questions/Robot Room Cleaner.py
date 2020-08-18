# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        
        def goBack():
            nonlocal robot
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
            
        def backTrack(cell = (0, 0), d = 0):
            nonlocal robot, directions, visited
            visited.add(cell)
            robot.clean()
            for i in range(4):
                newd = (d + i) % 4
                newCell = (cell[0] + directions[newd][0], cell[1] + directions[newd][1])
                if newCell not in visited and robot.move():
                    backTrack(newCell, newd)
                    goBack()
                robot.turnRight()
        
        backTrack()