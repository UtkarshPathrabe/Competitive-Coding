class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols, result = len(box), len(box[0]), []
        for r in range(rows):
            for c in range(cols - 2, -1, -1):
                if box[r][c] == '#':
                    finalIndex = c + 1
                    while finalIndex < cols and box[r][finalIndex] == '.':
                        finalIndex += 1
                    if box[r][finalIndex - 1] == '.':
                        box[r][c], box[r][finalIndex - 1] = box[r][finalIndex - 1], box[r][c]
        for c in range(cols):
            row = []
            for r in range(rows):
                row.append(box[r][c])
            result.append(row[::-1])
        return result