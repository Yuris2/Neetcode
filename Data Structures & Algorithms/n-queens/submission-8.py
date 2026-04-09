class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pDiag = set()
        nDiag = set()

        res = []
        board = [['.'] * n for i in range(n)]

        def back(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return res
            
            for c in range(n):
                pos, neg = (r + c), (r - c)
                if c in col or pos in pDiag or neg in nDiag:
                    continue
                
                board[r][c] = 'Q'
                col.add(c)
                pDiag.add(pos)
                nDiag.add(neg)

                back(r + 1)

                board[r][c] = '.'
                col.remove(c)
                pDiag.remove(pos)
                nDiag.remove(neg)
        
        back(0)
        return res
                

        