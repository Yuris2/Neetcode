import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        minHeap = [(0, points[0])]
        seen = set()

        res = 0

        while len(seen) != len(points):
            cost, point = heapq.heappop(minHeap)
            x1,y1 = point

            if (x1, y1) in seen:
                continue
            
            res += cost
            seen.add((x1,y1))

            for x2, y2 in points:
                if (x2, y2) not in seen:
                    c = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (c, (x2, y2)))
        
        return res




        