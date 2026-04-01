class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        res = []

        LEFT, RIGHT, DOWN, UP = 0,1,2,3
        direction = RIGHT

        lWall, rWall, upWall, dWall = -1, n, 0, m
        r,c = 0,0

        while len(res) < (m * n):
            if direction == RIGHT:
                while c < rWall:
                    res.append(matrix[r][c])
                    c += 1
                r,c = r + 1, c - 1
                direction = DOWN
                rWall -=1
            elif direction == LEFT:
                while c > lWall:
                    res.append(matrix[r][c])
                    c -= 1
                r,c = r - 1, c + 1
                direction = UP  
                lWall += 1
            elif direction == DOWN:
                while r < dWall:
                    res.append(matrix[r][c])
                    r += 1
                r,c = r - 1, c - 1
                direction = LEFT 
                dWall -= 1
            elif direction == UP:
                while r > upWall:
                    res.append(matrix[r][c])
                    r -= 1
                r,c = r + 1, c + 1
                direction = RIGHT
                upWall += 1
        return res
        