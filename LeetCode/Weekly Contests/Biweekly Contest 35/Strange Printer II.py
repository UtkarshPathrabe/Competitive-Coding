class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        colors, rows, cols = set(), len(targetGrid), len(targetGrid[0])
        for r in range(rows):
            for c in range(cols):
                colors.add(targetGrid[r][c])
        colorPositions = [[float('inf'), float('inf'), float('-inf'), float('-inf')] for _ in range(max(colors) + 1)] # left, top, right, bottom
        for r in range(rows):
            for c in range(cols):
                color = targetGrid[r][c]
                colorPositions[color][0] = min(colorPositions[color][0], c)
                colorPositions[color][1] = min(colorPositions[color][1], r)
                colorPositions[color][2] = max(colorPositions[color][2], c)
                colorPositions[color][3] = max(colorPositions[color][3], r)
        
        def isTopColor(color):
            for r in range(colorPositions[color][1], colorPositions[color][3] + 1):
                for c in range(colorPositions[color][0], colorPositions[color][2] + 1):
                    if targetGrid[r][c] > 0 and targetGrid[r][c] != color:
                        return False
            for r in range(colorPositions[color][1], colorPositions[color][3] + 1):
                for c in range(colorPositions[color][0], colorPositions[color][2] + 1):
                    targetGrid[r][c] = 0
            return True
        
        while colors:
            nonTopColors = set()
            for color in colors:
                if not isTopColor(color):
                    nonTopColors.add(color)
            if len(colors) == len(nonTopColors):
                return False
            colors = nonTopColors
        return True