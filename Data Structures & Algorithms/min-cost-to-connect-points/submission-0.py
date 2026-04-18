import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #The cost of connecting (x1,y1) and (x2,y2) is
            #|x1- x2| + |y1 - y2|
        #Return the minimum cost to connect all points
        if not points:
            return 0
        
        seen = set()
        res = 0
        #cost, pint
        heap = [(0, points[0])]

        while len(seen) != len(points):
            c, point = heapq.heappop(heap)
            x1,y1 = point

            if (x1, y1) in seen:
                continue
            
            seen.add((x1,y1))
            res += c

            for x2, y2 in points:
                cost = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(heap, (cost, (x2, y2)))
        
        return res




        #Start with any point
        #Push all its edges into a min heap
        #Pop the cheapest edge
        #Add to MST and repeat if neighbors is not in seen
        