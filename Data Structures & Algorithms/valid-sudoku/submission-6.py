import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R,C = len(board), len(board[0])
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        for r in range(R):
            for c in range(C):
                coord = board[r][c]

                if coord == ".":
                    continue
                
                if (coord in rowSet[r] 
                or coord in colSet[c] 
                or coord in squareSet[(r // 3, c // 3)]):
                    return False
                
                rowSet[r].add(coord)
                colSet[c].add(coord)
                squareSet[(r // 3, c // 3)].add(coord)
        
        return True

        



        