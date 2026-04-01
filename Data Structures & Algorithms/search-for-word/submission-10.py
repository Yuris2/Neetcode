class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])

        def dfs(x, y, i):
            if i == len(word):
                return True
            #Check bounds
            if x >= ROW or y >= COL or x < 0 or y < 0 or board[x][y] != word[i] or board[x][y] == '#':
                return False
            
            board[x][y] = "#"
            
            res = dfs(x + 1, y, i + 1) or  dfs(x - 1, y, i + 1) or  dfs(x, y + 1, i + 1) or  dfs(x, y - 1, i + 1) 

            board[x][y] = word[i]
            return res 
        

        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0):
                    return True
        
        return False
        



        