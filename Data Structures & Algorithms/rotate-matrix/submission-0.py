class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        R,C = len(matrix), len(matrix[0])

        #Transpose (swap (i,j) to (j,i))
        for r in range(R):
            for c in range(r + 1, C):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp
        
        #Horizontal Reflection 
        for r in range(R):
            #Only need to go half way
            for c in range(C // 2):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[r][-c - 1]
                matrix[r][-c - 1] = tmp

                    