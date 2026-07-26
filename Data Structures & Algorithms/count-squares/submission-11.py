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
        x1,y1 = point

        for x2 in self.plane:
            dist1 = abs(x2 - x1)

            if dist1 == 0:
                continue

            for y2 in self.plane[x2]:
                dist2 = abs(y2 - y1)

                if dist2 == 0 or dist1 != dist2:
                    continue
                
                if self.exists(x1,y2) and self.exists(x2,y1):
                    res += self.plane[x1][y2] * self.plane[x2][y2] * self.plane[x2][y1]
        
        return res

    def exists(self,x,y):
        if x in self.plane:
            if y in self.plane[x]:
                return True
        return False

        
