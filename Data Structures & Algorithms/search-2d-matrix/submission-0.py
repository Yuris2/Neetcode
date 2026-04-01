class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COL = len(matrix[0])

        l = 0
        r = ROWS * COL - 1

        while l <= r:
            m = (l + r) // 2

            x, y = m // COL, m % COL

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False


        