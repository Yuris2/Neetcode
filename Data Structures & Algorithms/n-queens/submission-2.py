class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() #(r + c)
        negDiag = set() #(r - c)

        res = []
        board = [['.'] * n for i in range(n)]

        def back(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            #Check valid col
            for c in range(n):
                neg, pos = (r - c), (r + c)

                #We can add a queen
                if c not in col and pos not in posDiag and neg not in negDiag:
                    #Stack.append()
                    board[r][c] = 'Q'
                    col.add(c)
                    posDiag.add(pos)
                    negDiag.add(neg)

                    back(r + 1)

                    board[r][c] = '.'
                    col.remove(c)
                    posDiag.remove(pos)
                    negDiag.remove(neg)
        
        back(0)
        return res

