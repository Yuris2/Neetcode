class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        R,C = len(matrix), len(matrix[0])

        for r in range(R):
            for c in range(r + 1, R):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp
        
        for r in range(R):
            for c in range(R // 2):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[r][-c - 1]
                matrix[r][-c - 1] = tmp
        
        