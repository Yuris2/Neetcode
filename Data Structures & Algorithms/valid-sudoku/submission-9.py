import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R,C = len(board), len(board[0])

        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        for r in range(R):
            for c in range(C):
                num = board[r][c]

                if num == '.':
                    continue
                
                if num in rowSet[r] or num in colSet[c]:
                    return False
                if num in squareSet[(r // 3, c // 3)]:
                    return False
                
                rowSet[r].add(num)
                colSet[c].add(num)
                squareSet[(r//3,c//3)].add(num)
        
        return True
