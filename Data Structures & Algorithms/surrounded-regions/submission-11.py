class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # mark regions that are unsurrounded 'T'
        # unmarked regions (surrounded) 'O' -> 'X'
        # uncapture unsurrounded regions
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r >= rows or c >= cols or
            r < 0 or c < 0 or board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'

            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                # edge and 'O'
                if ((r in [0, rows - 1] or c in [0, cols - 1]) and
                board[r][c] == 'O'):
                    capture(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'       
                


