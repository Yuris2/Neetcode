import collections
class CountSquares:
    def __init__(self):
        self.plane = defaultdict(dict)
    
    def add(self, point):
        x,y = point
        if y not in self.plane[x]:
            self.plane[x][y] = 1
        else:
            self.plane[x][y] += 1
    
    def count(self, point):
        qx, qy = point
        res = 0

        for x in self.plane:
            dx = abs(x - qx)

            if dx < 1:
                continue
            
            for y in self.plane[x]:
                dy = abs(y - qy)

                if dy < 1:
                    continue
                
                if dx == dy and self.exists(x,qy) and self.exists(qx, y):
                    res += (self.plane[qx][y] * self.plane[x][qy] * self.plane[x][y])
        
        return res
    
    def exists(self, x, y):
        if x in self.plane:
            if y in self.plane[x]:
                return True
        return False

        
