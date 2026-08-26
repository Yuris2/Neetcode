class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        firstRow, firstCol = False, False
        #Iterate through the firstRow and firstCol
        for r in range(m):
            for c in range(n):
                if matrix[r][c] != 0:
                    continue

                if r == 0 or c == 0:
                    if r == 0:
                        firstRow = True
                    if c == 0:
                        firstCol = True

                matrix[0][c] = 0
                matrix[r][0] = 0
        
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if firstRow:
            for c in range(n):
                matrix[0][c] = 0
        
        if firstCol:
            for r in range(m):
                matrix[r][0] = 0
        