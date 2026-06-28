import collections
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        goal = (R - 1, C - 1)
        seen = set()

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if (r,c) in seen:
                return False
            return True
        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        heap = [(grid[0][0],0,0)]

        while heap:
            cost,r,c = heapq.heappop(heap)

            if (r,c) == goal:
                return cost
            if (r,c) in seen:
                continue
            
            seen.add((r,c))
            for dr,dc in directions:
                nR,nC = r + dr, c + dc
                if isValid(nR, nC):
                    cst = max(cost,grid[nR][nC])
                    heapq.heappush(heap, (cst,nR,nC))
        
        return -1

        