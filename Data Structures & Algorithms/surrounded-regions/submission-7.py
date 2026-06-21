class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R,C = len(board), len(board[0])

        def dfs(r,c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return 
            if board[r][c] != 'O':
                return 
            board[r][c] = '#'

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        for r in range(R):
            for c in range(C):
                if r in [0, R - 1] or c in [0, C -1]:
                    dfs(r,c)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] != '#':
                    board[r][c] = 'X'
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == '#':
                    board[r][c] = 'O'
