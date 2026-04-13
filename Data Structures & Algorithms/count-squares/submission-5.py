import collections
class CountSquares:

    def __init__(self):
        self.plane = defaultdict(dict)
        
    def add(self, point: List[int]) -> None:
        x,y = point

        if y in self.plane[x]:
            self.plane[x][y] += 1
        else:
            self.plane[x][y] = 1        

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0

        for dx in self.plane:
            side1 = abs(qx - dx)

            if side1 == 0:
                continue
            
            for dy in self.plane[dx]:
                side2 = abs(qy - dy)

                if side1 == side2 and self.exists(qx, dy) and self.exists(dx, qy):
                    res += self.plane[dx][dy] * self.plane[dx][qy] * self.plane[qx][dy]
        
        return res

    def exists(self,x,y):
        if x in self.plane:
            if y in self.plane[x]:
                return True
        return False
        
