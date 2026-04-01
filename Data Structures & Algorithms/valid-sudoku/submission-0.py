import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                square = board[r][c]

                if square == ".":
                    continue
                
                if square in rows[r] or square in columns[c] or square in squares[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(square)
                columns[c].add(square)
                squares[(r // 3 , c //3)].add(square)
        
        return True
                
        