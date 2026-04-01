class Solution:
    def solveNQueens(self, ni: int) -> List[List[str]]:
        col = set()
        pos = set()
        neg = set()

        res = []
        board = [['.'] * ni for i in range(ni)]
        
        def back(r):
            #At every row, we want to choose a place
            #where we can insert a valid queen
            #If we can make it to the end
            if r >= ni:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(ni):
                p = (r + c)
                n = (r - c)

                if c not in col and p not in pos and n not in neg:
                    #Mark as seen (stack.append)
                    board[r][c] = 'Q'
                    col.add(c)
                    pos.add(p)
                    neg.add(n)

                    #Backtrack to next row
                    back(r + 1)

                    #Pop from stack
                    board[r][c] = '.'
                    col.remove(c)
                    pos.remove(p)
                    neg.remove(n)
        
        back(0)
        return res
