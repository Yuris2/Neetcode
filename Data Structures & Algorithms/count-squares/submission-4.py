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
            s1 = abs(dx - qx)

            if s1 == 0:
                continue
            
            for dy in self.plane[dx]:
                s2 = abs(dy - qy)

                if s2 == s1 and self.exist(dx,qy) and self.exist(qx, dy):
                    res += self.plane[dx][qy] * self.plane[dx][dy] * self.plane[qx][dy]
        
        return res
    
    def exist(self, x, y):
        if x in self.plane:
            if y in self.plane[x]:
                return True
        return False        
