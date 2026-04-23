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
        res = 0
        x,y = point

        for dx in self.plane:
            side1 = abs(dx - x)
            if side1 == 0:
                continue
            
            for dy in self.plane[dx]:
                side2 = abs(dy - y)
                if side2 == 0:
                    continue
                
                if side1 == side2 and self.exists(dx,y) and self.exists(x, dy):
                    res += self.plane[dx][y] * self.plane[dx][dy] * self.plane[x][dy]
        
        return res
    
    def exists(self, x, y):
        if x in self.plane:
            if y in self.plane[x]:
                return True
        return False

        
