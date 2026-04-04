class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Rows
        m = len(matrix)
        #Columns
        n = len(matrix[0])

        #Run Binary Search on the Matrix
        #Treat the entire array as a single array

        l, r = 0, m * n - 1

        #m = 3
        #n = 4

        #6 => (1, 2)
        while l <= r:
            m = (l + r) // 2

            x = m // n
            y = m % n

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False


        