import collections
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #If a matrix is 0, set its column and row to 0 in place
        m,n = len(matrix), len(matrix[0])

        #We can use the start of column and row to replace these sets 
        #But we need a variable to track if anything in row1/col1 = 0
        row1,col1 = False, False


        for r in range(m):
            for c in range(n):
                if (r == 0 or c == 0) and matrix[r][c] == 0:
                    if r == 0:
                        row1 = True
                    if c == 0:
                        col1 = True
                elif matrix[r][c] == 0:
                    #Marking that these row/col need to be 0
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        #Avoid overwriting markers so start at 1
        for r in range(1, m):
            for c in range(1,n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if row1:
            for c in range(n):
                matrix[0][c] = 0
        if col1:
            for r in range(m):
                matrix[r][0] = 0
        #Solution Intuition
            #Iteration #1
                #Use a set to keep track of which coord need to be set to 0
                #This does not include the new column and row
            #Iteration #2
                #Set these coordinates to 0


        
        