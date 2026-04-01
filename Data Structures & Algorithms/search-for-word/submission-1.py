class Solution:
    def exist(self, board, word):
        ROW = len(board)
        COL = len(board[0])
        #Takes in a 2D Array
        #Takes in a word
        #Returns true if that word is on the board

        #Go through every element in board from top to bottom
        #Check if the character is the first letter on the board
            #If not, skip over letter
            #If is, check surrounding area
                #DFS
        #Return if word is present

        def dfs(r,c,i):
            if i == len(word):
                return True
            #IN Bounds
            #Valid char
            if r < 0 or r >= ROW or c < 0 or c >= COL or word[i] != board[r][c] or board[r][c] == '#':
                return False
            #NO POUNDS
            board[r][c] = '#'

            res = (dfs(r - 1,c, i + 1) or
                dfs(r + 1,c, i + 1) or 
                dfs(r,c - 1, i + 1) or
                dfs(r,c + 1, i + 1))
            
            board[r][c] = word[i]

            return res

            
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0):
                    return True
        
        return False