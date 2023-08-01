"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def constructTreeHelper(rowStart, rowEnd, colStart, colEnd):
            values = set(cellValue for row in grid[rowStart: rowEnd] for cellValue in row[colStart: colEnd])
            if len(values) == 1:
                return Node(grid[rowStart][colStart], True, None, None, None, None)
            rowMid = (rowStart + rowEnd) >> 1
            colMid = (colStart + colEnd) >> 1
            topLeftChild = constructTreeHelper(rowStart, rowMid, colStart, colMid)
            topRightChild = constructTreeHelper(rowStart, rowMid, colMid, colEnd)
            bottomLeftChild = constructTreeHelper(rowMid, rowEnd, colStart, colMid)
            bottomRightChild = constructTreeHelper(rowMid, rowEnd, colMid, colEnd)
            return Node(1, False, topLeftChild, topRightChild, bottomLeftChild, bottomRightChild)
        return constructTreeHelper(0, n, 0, n)