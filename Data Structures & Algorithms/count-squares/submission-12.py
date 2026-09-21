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
        x,y = point
        res = 0

        for xi in self.plane:
            dist1 = abs(x - xi)
            if dist1== 0:
                continue
            
            for yi in self.plane[xi]:
                dist2 = abs(y - yi)
                if dist2 == 0:
                    continue

                if dist1 == dist2 and self.exists(x,yi) and self.exists(xi,y):
                    res += self.plane[x][yi] * self.plane[xi][y] * self.plane[xi][yi]
                
        return res

    
    def exists(self,x,y):
        if x in self.plane:
            if y in self.plane[x]:
                return True
        
        return False
        
