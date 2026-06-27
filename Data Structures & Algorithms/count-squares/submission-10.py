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
        xi,yi = point
        res = 0

        for xj in self.plane:
            dist1 = abs(xi - xj)

            if dist1 == 0:
                continue 
            for yj in self.plane[xj]:
                dist2 = abs(yi - yj)

                if dist2 < 0 or dist1 != dist2:
                    continue
                if self.exists(xi,yj) and self.exists(xj,yi):
                    res += self.plane[xj][yj] * self.plane[xi][yj] * self.plane[xj][yi]
        
        return res
                
    
    def exists(self,x,y):
        if x in self.plane:
            if y in self.plane[x]:
                return True
        return False
        
