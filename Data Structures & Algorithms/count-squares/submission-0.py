#Add new points, duplicate points treated as separate points
#Query - count the number of ways to choose three additional points
    #3 points must form a square (no diagonal)
import collections
class CountSquares:
    '''{
    X: {y:count}
    
    
    }
    
    '''
    def __init__(self):
        #Since we want to track occurences of a point
        #We need to not only track what points were added to the X
        
        #We need to track given those points on the X, how many times does a Y appear as well
        #^To deal with duplicate

        #X:{Y:Count}
        self.plane = defaultdict(dict)

        
    #Add new points (Dupes Treated as Separate Points)
    def add(self, point: List[int]) -> None:
        x,y = point

        if y in self.plane[x]:
            self.plane[x][y] += 1
        else:
            self.plane[x][y] = 1
        

        
        
    #Count the number of ways to choose 3 points to form a square
    def count(self, point: List[int]) -> int:
        #You only need one point (Diagonal)
        #Horizontal and Vertical Distance from Query to Diagonal have to be equal
        res = 0
        qx, qy = point

        #Iterating over each x that was added
        for dx in self.plane:
            side1 = abs(dx - qx)
            #Check for candidate diagonals
            if side1 == 0:
                continue
            #Iterate over the possible y's
            for dy in self.plane[dx]:
                #Valid Square (dx, dy)
                if abs(dy - qy) == side1:
                    #Check if (dx, qy) and (qx, dy) are valid
                    if self.exists(dx,qy) and self.exists(qx,dy):
                        res += (self.plane[dx][qy] * self.plane[qx][dy] * self.plane[dx][dy])
        
        return res

    
    def exists(self, x, y):
        if x in self.plane:
            if y in self.plane[x]:
                return True
        return False

                        


        

        
