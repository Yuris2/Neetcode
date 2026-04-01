class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R,C = len(matrix), len(matrix[0])
        #Treat the 2D Matrix as a single 1D Matrix
        l = 0
        r = R * C - 1

        while l <= r:
            #Calculate midpoint as if it was one array
            m = (l + r) // 2

            #Calculate the Row and Col # (Convert into coords)
            x = m // C
            y = m % C

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False


        