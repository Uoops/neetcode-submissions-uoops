class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        row_seen = [set() for _ in range(rows)]
        col_seen = [set() for _ in range(cols)]
        sub_seen = [set() for _ in range(9)]

        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val == ".":
                    continue
                
                box_idx = (r // 3) * 3 + (c // 3)
                if val in row_seen[r] or val in col_seen[c] or val in sub_seen[box_idx]:
                    return False

                row_seen[r].add(val)
                col_seen[c].add(val)
                sub_seen[box_idx].add(val)
        
        return True