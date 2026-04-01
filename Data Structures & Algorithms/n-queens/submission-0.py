class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        #(R+C)
        posDiag = set()
        #(R-C)
        negDiag = set()

        res = []
        #Stack
        board = [["."] * n for i in range(n)]

        def back(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            #Go through every column
            for c in range(n):
                if(c not in col and (r + c) not in posDiag and 
                (r - c) not in negDiag):
                    #stack.append
                    board[r][c] = 'Q'
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)

                    back(r + 1)

                    #stack.pop()
                    board[r][c] = '.'
                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
        
        back(0)
        return res        
