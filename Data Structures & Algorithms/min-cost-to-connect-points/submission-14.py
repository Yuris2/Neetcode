import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        x,y = points[0][0], points[0][1]
        seen = set()
        heap = [[0,x,y]]

        while len(seen) != len(points):
            cost, xi,yi = heapq.heappop(heap)

            if (xi, yi) in seen:
                continue

            res += cost
            seen.add((xi,yi))

            for xj,yj in points:
                if (xj, yj) not in seen:
                    cost = abs(xj - xi) + abs(yj - yi)
                    heapq.heappush(heap, [cost, xj, yj])
        
        return res
        