class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                elem = board[r][c]

                if elem == '.':
                    continue

                if elem in rows[r] or elem in cols[c] or elem in square[(r // 3,c // 3)]:
                    return False
                
                rows[r].add(elem)
                cols[c].add(elem)
                square[(r // 3,c // 3)].add(elem)
        
        return True


        