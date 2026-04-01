class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        for x in range(len(board)):
            for y in range(len(board[x])):
                coord = board[x][y]

                if coord == ".":
                    continue
                
                if coord in rowSet[x] or coord in colSet[y] or coord in squareSet[(x // 3, y // 3)]:
                    return False

                rowSet[x].add(coord)
                colSet[y].add(coord)
                squareSet[(x // 3, y // 3)].add(coord)
        
        return True
        