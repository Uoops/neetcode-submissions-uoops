from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        
        pres = self.bfs(pacific, rows, cols, heights)
        ares = self.bfs(atlantic, rows, cols, heights)

        combine = pres & ares
        return [list(pair) for pair in combine]

    def bfs(self, inputs, rows, cols, grid):
        queue = deque(inputs)
        visited = set(inputs)

        while queue:
            r, c = queue.popleft()
            val = grid[r][c]
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] >= val and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        return visited