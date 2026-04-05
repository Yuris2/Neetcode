class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        #Transpose
        for r in range(n):
            for c in range(r, n):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

        for r in range(n):
            for c in range(n // 2):
                temp = matrix[r][c]
                matrix[r][c] = matrix[r][-c - 1]
                matrix[r][-c - 1] = temp

        