class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        
        res = []
        board = [['.'] * n for i in range(n)]

        def back(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                pD, nD = (r + c), (r - c)

                if (
                    c not in col and 
                    pD not in posDiag and
                    nD not in negDiag
                    ):

                    board[r][c] = 'Q'
                    col.add(c)
                    negDiag.add(nD)
                    posDiag.add(pD)

                    back(r + 1)

                    board[r][c] = '.'
                    col.remove(c)
                    negDiag.remove(nD)
                    posDiag.remove(pD)
        
        back(0)
        return res


        