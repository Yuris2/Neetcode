class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        def capture(r,c):
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return
            elif board[r][c] != 'O':
                return
            
            board[r][c] = '#'

            capture(r + 1,c)
            capture(r - 1,c)
            capture(r,c + 1)
            capture(r,c - 1)
        
        #Around the perimeter capture
        for r in range(ROW):
            for c in range(COL):
                if r in [0, ROW - 1] or c in [0, COL - 1]:
                    capture(r,c)
        
        #Converting all O's into X
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == '#':
                    board[r][c] = 'O'
        
