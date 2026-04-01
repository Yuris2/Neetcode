class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for r in range(n):
            for c in range(r + 1, n):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp
        
        for r in range(n):
            for c in range(n // 2):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[r][-c - 1]
                matrix[r][-c - 1] = tmp