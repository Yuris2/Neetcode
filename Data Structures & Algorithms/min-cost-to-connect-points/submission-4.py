import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        start = points[0]
        minHeap = [(0, start[0], start[1])]
        res = 0

        while len(seen) != len(points):
            cost, x1, y1 = heapq.heappop(minHeap)

            if (x1, y1) in seen:
                continue
            
            res += cost
            seen.add((x1, y1))

            for x2, y2 in points:
                if (x2, y2) not in seen:
                    cost = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (cost, x2, y2))
        
        return res


            
            
        