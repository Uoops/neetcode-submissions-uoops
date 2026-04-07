class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for dr, dc in neighbors:
                        nr = r + dr
                        nc = c + dc
                        if not 0 <= nr < rows or not 0 <= nc < cols or grid[nr][nc] == 0:
                            result += 1
        
        return result