import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)    

        for r in range(len(board)):
            for c in range(len(board[0])):
                square = board[r][c]

                if square == '.':
                    continue

                if square in rowSet[r] or square in colSet[c] or square in squareSet[(r // 3, c // 3)]:
                    return False

                rowSet[r].add(square)
                colSet[c].add(square)
                squareSet[(r//3,c//3)].add(square) 

        return True   