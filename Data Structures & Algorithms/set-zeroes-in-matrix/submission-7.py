class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R,C = len(matrix), len(matrix[0])

        firstRow, firstCol = False, False

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0 and (r == 0 or c == 0):
                    if r == 0:
                        firstRow = True
                    if c == 0:
                        firstCol = True
                elif matrix[r][c] == 0:
                    matrix[0][c], matrix[r][0] = 0,0
        
        for r in range(1,R):
            for c in range(1,C):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if firstRow:
            for c in range(C):
                matrix[0][c] = 0
        
        if firstCol:
            for r in range(R):
                matrix[r][0] = 0
                    
        
        