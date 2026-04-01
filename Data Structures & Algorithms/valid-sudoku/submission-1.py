import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                square = board[r][c]

                if square == '.':
                    continue
                
                if square in colSet[c] or square in rowSet[r] or square in squareSet[(r // 3, c // 3)]:
                    return False
                
                colSet[c].add(square)
                rowSet[r].add(square)
                squareSet[(r // 3, c // 3)].add(square)
        
        return True


        