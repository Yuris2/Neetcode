class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        row = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [['.'] * n for _ in range(n)]

        def back(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                pD, nD = (r + c), (r - c)

                if c in col or r in row or pD in posDiag or nD in negDiag:
                    continue
                
                board[r][c] = 'Q'
                col.add(c)
                row.add(r)
                posDiag.add(pD)
                negDiag.add(nD)
                back(r + 1)

                board[r][c] = '.'
                col.remove(c)
                row.remove(r)
                posDiag.remove(pD)
                negDiag.remove(nD)
        
        back(0)
        return res
            

        