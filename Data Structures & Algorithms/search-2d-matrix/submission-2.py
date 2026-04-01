class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        l = 0
        r = R * C - 1

        while l <= r:
            m = (l + r) // 2

            x,y = m // C, m % C

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
        
        