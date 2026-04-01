class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos = set()
        neg = set()

        res = []
        board = [['.'] * n for i in range(n)]

        def back(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                p, e = (r + c), (r - c)

                if c not in col and p not in pos and e not in neg:
                    board[r][c] = 'Q'
                    col.add(c)
                    pos.add(p)
                    neg.add(e)

                    back(r + 1)

                    board[r][c] = '.'
                    col.remove(c)
                    pos.remove(p)
                    neg.remove(e)
        back(0)
        return res
        