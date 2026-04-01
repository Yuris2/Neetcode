class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        RIGHT, LEFT, UP, DOWN = 0,1,2,3

        lWall = -1
        rWall = n
        upWall = 0
        bWall = m

        res = []
        direction = RIGHT

        r,c = 0,0
        while len(res) < m * n:
            if direction == RIGHT:
                while c < rWall:
                    res.append(matrix[r][c])
                    c += 1
                r, c = r + 1, c - 1
                direction = DOWN
                rWall -= 1
            elif direction == DOWN:
                while r < bWall:
                    res.append(matrix[r][c])
                    r += 1
                r, c = r - 1, c - 1
                direction = LEFT
                bWall -= 1
            elif direction == LEFT:  
                while c > lWall:
                    res.append(matrix[r][c])
                    c -= 1
                r, c = r - 1, c + 1
                direction = UP
                lWall += 1                                              
            elif direction == UP:
                while r > upWall:
                    res.append(matrix[r][c])
                    r -= 1
                r, c = r + 1, c + 1
                direction = RIGHT
                upWall += 1

        return res            


        