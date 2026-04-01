class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos = set()
        neg = set()

        board = [['.'] * n for i in range(n)]
        res = []

        def back(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                nD,pD = (r - c), (r + c)

                if c not in col and pD not in pos and nD not in neg:
                    board[r][c] = 'Q'
                    pos.add(pD)
                    neg.add(nD)
                    col.add(c)

                    back(r + 1)

                    board[r][c] = '.'
                    pos.remove(pD)
                    neg.remove(nD)
                    col.remove(c)
        
        back(0)
        return res
                    
        