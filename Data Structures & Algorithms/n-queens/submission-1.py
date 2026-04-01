class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def back(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            #Try placing the queen in every column 
            for c in range(n):
                pos, neg = r + c, r - c

                if (c not in col and 
                pos not in posDiag and neg not in negDiag):
                    #Backtrack
                    board[r][c] = "Q"
                    col.add(c)
                    posDiag.add(pos)
                    negDiag.add(neg)

                    back(r + 1)

                    #Undo
                    board[r][c] = "."
                    col.remove(c)
                    posDiag.remove(pos)
                    negDiag.remove(neg)
        
        back(0)
        return res

        