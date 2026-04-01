import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R, C = len(board), len(board[0])
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        def exists(r,c):
            if board[r][c] in rowSet[r]:
                return True
            elif board[r][c] in colSet[c]:
                return True
            elif board[r][c] in squareSet[(r // 3,c // 3)]:
                return True
            return False
    
        for r in range(R):
            for c in range(C):
                square = board[r][c]

                if square == '.':
                    continue
                
                if exists(r,c):
                    return False
                
                colSet[c].add(square)
                rowSet[r].add(square)
                squareSet[(r // 3,c // 3)].add(square)
                
        return True

        