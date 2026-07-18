class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0]) 
        res = []
        r,c = 0,0

        L,R,D,U = 0,1,2,3
        lWall,rWall,uWall, dWall = -1,n,0,m

        direction = R

        while len(res) < (m * n):
            if direction == R:
                while c < rWall:
                    res.append(matrix[r][c])
                    c += 1
                r,c = r + 1, c - 1
                rWall -= 1
                direction = D
            elif direction == D:
                while r < dWall:
                    res.append(matrix[r][c])
                    r += 1
                r,c = r - 1, c - 1
                dWall -= 1
                direction = L
            elif direction == L:
                while c > lWall:
                    res.append(matrix[r][c])
                    c -= 1
                r,c = r - 1, c + 1
                lWall += 1
                direction = U
            elif direction == U:
                while r > uWall:
                    res.append(matrix[r][c])
                    r -= 1
                r,c = r + 1, c + 1
                uWall += 1
                direction = R
        return res
        