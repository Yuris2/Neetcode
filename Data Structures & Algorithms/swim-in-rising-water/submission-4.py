import collections
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        minHeap =[(grid[0][0], (0, 0))]
        seen = {(0,0)}

        goal = (R - 1, C - 1)
        direction = [[1,0], [0,1], [-1,0], [0,-1]]

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if (r,c) in seen:
                return False
            return True

        while minHeap:
            cost, point = heapq.heappop(minHeap)
            r,c = point

            if point == goal:
                return cost
            
            for dr,dc in direction:
                nR, nC = dr + r, dc + c

                if isValid(nR,nC):
                    cst = max(cost, grid[nR][nC])
                    seen.add((nR, nC))
                    heapq.heappush(minHeap, (cst, (nR, nC)))
        
        return -1
            

        