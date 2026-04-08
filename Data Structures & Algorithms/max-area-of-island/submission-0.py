class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                res = max(res, self.dfs(r, c, rows, cols, grid))
        
        return res
    
    def dfs(self, r, c, rows, cols, grid):
        if grid[r][c] == 0:
            return 0

        grid[r][c] = 0
        neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = 0
        for dr, dc in neighbors:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                res += self.dfs(nr, nc, rows, cols, grid)
        
        return res + 1
