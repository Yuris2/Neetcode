import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        heap = [[0, points[0][0], points[0][1]]]
        res = 0

        while len(seen) != len(points):
            cost, xi, yi = heapq.heappop(heap)

            if (xi,yi) in seen:
                continue
            
            seen.add((xi,yi))
            res += cost

            for xj, yj in points:
                if (xj,yj) not in seen:
                    dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(heap, (dist, xj, yj))

        return res
    
        