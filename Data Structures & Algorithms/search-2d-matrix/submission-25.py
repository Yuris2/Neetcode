class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        top,bottom = 0, len(matrix) - 1
        #Run binary Search on the Rows
        while top <= bottom:
            m = (top + bottom) // 2

            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bottom = m - 1
            else:
                row = m
                break
        
        left, right = 0, len(matrix[0]) - 1
        #Run binary Search on the Columns
        while left <= right:
            m = (left + right) // 2

            if matrix[row][m] > target:
                right = m - 1
            elif matrix[row][m] < target:
                left = m + 1
            else:
                return True
        
        return False
        