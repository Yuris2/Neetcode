class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m,n = len(matrix), len(matrix[0])

        #Directions
        L,R,D,U = 0,1,2,3
        direction = R

        lWall, rWall, dWall, uWall = -1, n, m, 0

        r,c = 0,0
        while len(res) < (m * n):
            if direction == R:
                while c < rWall:
                    res.append(matrix[r][c])
                    c += 1
                r,c = r + 1, c - 1
                direction = D
                rWall -= 1 
            elif direction == D:
                while r < dWall:
                    res.append(matrix[r][c])
                    r += 1
                r,c = r - 1, c - 1
                direction = L
                dWall -= 1 
            elif direction == L:
                while c > lWall:
                    res.append(matrix[r][c])
                    c -= 1
                r,c = r - 1, c + 1
                direction = U
                lWall += 1 
            elif direction == U:
                while r > uWall:
                    res.append(matrix[r][c])
                    r -= 1
                r,c = r + 1, c + 1
                direction = R
                uWall += 1 
        return res
        