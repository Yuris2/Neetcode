class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COL = len(board[0])

        def dfs(x, y, c):
            if c == len(word):
                return True

            if x < 0 or y < 0 or y >= COL or x >= ROWS or board[x][y] != word[c] or board[x][y] == '#':
                return False
            
            board[x][y] = '#'
            
            res = dfs(x + 1, y, c + 1) or dfs(x, y + 1, c + 1) or dfs(x - 1, y, c + 1) or dfs(x, y - 1, c + 1)

            board[x][y] = word[c]

            return res


        
        for r in range(ROWS):
            for c in range(COL):
                if dfs(r,c,0):
                    return True

        return False

        