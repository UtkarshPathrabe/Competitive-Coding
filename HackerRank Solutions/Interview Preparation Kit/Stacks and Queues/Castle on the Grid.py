#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    availableMoves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = set((startX, startY))
    queue = [[startX, startY, 0]]
    while len(queue) > 0:
        currentPath, queue = queue[0], queue[1:]
        currentX, currentY, distanceTravelled = currentPath
        for move in availableMoves:
            newX, newY = currentX, currentY
            while True:
                newX, newY = newX + move[0], newY + move[1]
                if newX > -1 and newX < len(grid) and newY > -1 and newY < len(grid) and grid[newX][newY] != 'X':
                    if (newX, newY) == (goalX, goalY):
                        return distanceTravelled + 1
                    else:
                        if (newX, newY) not in visited:
                            visited.add((newX, newY))
                            queue += [[newX, newY, distanceTravelled + 1]]
                else:
                    break
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
