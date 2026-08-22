class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R,C = len(matrix), len(matrix[0])

        top = 0
        bot = R - 1
        row = -2e9

        #Binary search on rows
        while top <= bot:
            #Row we are on
            r = (top + bot) // 2
            row = r
            #If target > last element of row
            if target > matrix[r][-1]:
                top = r + 1
            elif target < matrix[r][0]:
                bot = r - 1
            else:
                
                break
        
        l = 0
        r = C - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False



        
        