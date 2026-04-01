import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Create an array with Euclidean distance
        #Calculating distance in respect to array index
        def distanceFromOrigin(x,y):
            return math.sqrt(x**2 + y**2)
        
        maxHeap = []
        res = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]

            distance = distanceFromOrigin(x,y)

            maxHeap.append([distance, i])
        
        heapq.heapify(maxHeap)

        elements = 0

        while elements != k:
            distance = heapq.heappop(maxHeap)
            res.append(points[distance[1]])
            elements += 1
        
        return res


            
            

        