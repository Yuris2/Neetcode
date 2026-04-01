class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        neg = set()
        pos = set()

        res = []
        board = [['.'] * n for i in range(n)]

        def back(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                pD, nD = (r + c), (r - c)

                if c not in col and pD not in pos and nD not in neg:
                    board[r][c] = 'Q'
                    col.add(c)
                    pos.add(pD)
                    neg.add(nD)

                    back(r + 1)

                    board[r][c] = '.'
                    col.remove(c)
                    pos.remove(pD)
                    neg.remove(nD)
        
        back(0)
        return res
        