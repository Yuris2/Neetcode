class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R,C = len(board), len(board[0])
        def capture(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            if board[r][c] != 'O':
                return
            
            board[r][c] = '#'

            capture(r+1,c)
            capture(r,c+1)
            capture(r-1,c)
            capture(r,c-1)
        
        for r in range(R):
            for c in range(C):
                if r in [0, R - 1] or c in [0, C - 1]:
                    capture(r,c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(R):
            for c in range(C):
                if board[r][c] == '#':
                    board[r][c] = 'O'
        
        