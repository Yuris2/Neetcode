import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        x,y = points[0]
        heap = [(0,x,y)]

        res = 0

        def manhattan(xi,yi,xj,yj):
            return abs(xi-xj) + abs(yi-yj)

        while heap:
            c,xi,yi = heapq.heappop(heap)

            if (xi,yi) in seen:
                continue
            
            res += c
            seen.add((xi,yi))
            
            for xj,yj in points:
                if (xj,yj) not in seen:
                    cst = manhattan(xi,yi,xj,yj)
                    heapq.heappush(heap,(cst,xj,yj))
        
        return res


