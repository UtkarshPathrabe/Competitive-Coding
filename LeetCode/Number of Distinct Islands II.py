class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        visited, shapes, shape = set(), set(), set()
        def dfsHelper(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] and (row, col) not in visited:
                visited.add((row, col))
                shape.add(complex(row, col))
                dfsHelper(row - 1, col)
                dfsHelper(row, col - 1)
                dfsHelper(row + 1, col)
                dfsHelper(row, col + 1)
        def canonical(shape):
            def translate(shape):
                minCoordinate = complex(min(z.real for z in shape), min(z.imag for z in shape))
                return sorted(str(z - minCoordinate) for z in shape)
            result = []
            for k in range(4):
                result = max(result, translate([z * (1j) ** k for z in shape]))
                result = max(result, translate([complex(z.imag, z.real) * (1j) ** k for z in shape]))
            return tuple(result)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                dfsHelper(r, c)
                if shape:
                    shapes.add(canonical(shape))
        return len(shapes)