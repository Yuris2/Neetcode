import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [[0, points[0][0], points[0][1]]]
        seen = set()
        res = 0

        while minHeap:
            cost, xi, yi = heapq.heappop(minHeap)

            if (xi,yi) in seen:
                continue
            
            res += cost
            seen.add((xi,yi))

            for xj, yj in points:
                if (xj, yj) not in seen:
                    manhattan = abs(xi-xj) + abs(yi - yj)
                    heapq.heappush(minHeap, (manhattan, xj, yj))
        
        return res

        
        