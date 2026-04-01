import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R,C = len(board), len(board[0])

        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        for r in range(R):
            for c in range(C):
                square = board[r][c]

                if square == '.':
                    continue
                
                if square in rowSet[r]:
                    return False
                elif square in colSet[c]:
                    return False
                elif square in squareSet[(r // 3, c // 3)]:
                    return False
                
                rowSet[r].add(square)
                colSet[c].add(square)
                squareSet[(r // 3, c // 3)].add(square)
        
        return True
        