class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m,n = len(matrix), len(matrix[0])

        LEFT,RIGHT,DOWN,UP = 0,1,2,3

        lWall, rWall, dWall, upWall = -1,n,m,0

        DIRECTION = RIGHT
        r,c = 0,0

        while len(res) < (m * n):
            if DIRECTION == RIGHT:
                while c < rWall:
                    res.append(matrix[r][c])
                    c += 1
                r,c = r + 1, c - 1
                rWall -= 1
                DIRECTION = DOWN  
            elif DIRECTION == DOWN:
                while r < dWall:
                    res.append(matrix[r][c])
                    r += 1
                r,c = r - 1, c - 1
                dWall -= 1
                DIRECTION = LEFT
            elif DIRECTION == LEFT:
                while c > lWall:
                    res.append(matrix[r][c])
                    c -= 1
                r,c = r - 1, c + 1
                lWall += 1
                DIRECTION = UP
            elif DIRECTION == UP:
                while r > upWall:
                    res.append(matrix[r][c])
                    r -= 1
                r,c = r + 1, c + 1
                upWall += 1
                DIRECTION = RIGHT
        
        return res
        