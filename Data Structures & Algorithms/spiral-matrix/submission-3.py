class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        res = []

        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        rWall, dWall, lWall, uWall = n, m, -1, 0

        r,c = 0,0
        direction = RIGHT
        while len(res) < ( m * n):
            if direction == RIGHT:
                while c < rWall:
                    res.append(matrix[r][c])
                    c += 1
                r,c = r + 1, c - 1
                rWall -= 1
                direction = DOWN
            elif direction == DOWN:
                while r < dWall:
                    res.append(matrix[r][c])
                    r += 1
                r,c = r - 1, c - 1
                dWall -= 1
                direction = LEFT
            elif direction == LEFT:
                while c > lWall:
                    res.append(matrix[r][c])
                    c -= 1
                r,c = r - 1, c + 1
                lWall += 1
                direction = UP
            elif direction == UP:
                while r > uWall:
                    res.append(matrix[r][c])
                    r -= 1
                r,c = r + 1, c + 1
                uWall += 1
                direction = RIGHT

        return res        
        
        