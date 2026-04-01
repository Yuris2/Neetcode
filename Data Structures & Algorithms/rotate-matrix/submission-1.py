class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        R,C = len(matrix), len(matrix[0])
        #Find the transpose of the matrix
        for r in range(R):
            for c in range(r,C):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp
        
        #Take the horizontal reverse
        for r in range(R):
            for c in range(C // 2):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[r][-c - 1]
                matrix[r][-c - 1] = tmp
        
        

        