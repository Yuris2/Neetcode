'''
Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
#0
#1
[1,0] flips with [0,1]
[2,0] flips with [0,2]
[1,2] flips with [2,1]

#reflect upon main diagonal
  [1,4,7],
  [2,5,8],
  [3,6,9]

#reflect upon midpoint
  [7,4,1],
  [8,5,2],
  [9,6,3]


'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        #Transpose of matrix
        for r in range(n):
            for c in range(r + 1, n):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp
        

        #Reflection of matrix
        for r in range(n):
            for c in range(n // 2):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[r][-c - 1]
                matrix[r][-c - 1] = tmp

    
        