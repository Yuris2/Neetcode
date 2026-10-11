import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        heap = [[0, points[0][0], points[0][1]]]
        res = 0

        while heap:
            cost, xi, yi = heapq.heappop(heap)

            if (xi, yi) in seen:
                continue

            res += cost
            seen.add((xi,yi))

            for xj, yj in points:
                if (xj, yj) not in seen:
                    cost = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(heap, (cost, xj, yj))
        
        return res




        