import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        start = points[0]
        minHeap = [(0, start[0], start[1])]
        seen = set()

        res = 0

        while len(seen) != n:
            cost, xi, yi = heapq.heappop(minHeap)
            
            if (xi, yi) in seen:
                continue
            
            seen.add((xi, yi))
            res += cost

            for xj, yj in points:
                if (xj, yj) not in seen:
                    c = abs(xj - xi) + abs(yj - yi)
                    heapq.heappush(minHeap, (c, xj, yj))
        
        return res

        


        