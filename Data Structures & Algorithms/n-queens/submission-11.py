class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        col = set()
        posDiag = set()
        negDiag = set()


        def back(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                pD = r + c
                nD = r - c

                if c in col or pD in posDiag or nD in negDiag:
                    continue
                
                board[r][c] = "Q"
                col.add(c)
                negDiag.add(nD)
                posDiag.add(pD)
                back(r + 1)

                board[r][c] = "."

                col.remove(c)
                negDiag.remove(nD)
                posDiag.remove(pD)

        back(0)
        return res


        