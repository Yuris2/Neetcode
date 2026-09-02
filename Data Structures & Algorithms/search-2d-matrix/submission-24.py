class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R,C = len(matrix), len(matrix[0])

        row = 0
        
        top, bottom = 0, R - 1

        while top <= bottom:
            m = (top + bottom) // 2

            if matrix[m][0] > target:
                bottom = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                row = m
                break
        
        l,r = 0, C - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        
        return False


        