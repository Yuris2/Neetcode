import collections
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #If a matrix is 0, set its column and row to 0 in place
        m,n = len(matrix), len(matrix[0])

        row = set()
        col = set()


        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)


        for r in range(m):
            for c in range(n):
                if r in row or c in col:
                    matrix[r][c] = 0 
        #Solution Intuition
            #Iteration #1
                #Use a set to keep track of which coord need to be set to 0
                #This does not include the new column and row
            #Iteration #2
                #Set these coordinates to 0


        
        