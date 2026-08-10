import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # [[dist from o, x, y]]
        dists = []
        for x, y in points: # [x, y]
            dist = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)
            dists.append([dist, x, y])
        
        heapq.heapify(dists)
        
        res = [] # [[x, y]]

        while len(res) < k:
            dist, x, y = heapq.heappop(dists)
            res.append([x, y])

        return res
        
