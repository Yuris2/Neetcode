import collections
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        heap = [[grid[0][0],0,0]]
        seen = set()

        directions = [[1,0],[0,1], [-1,0], [0,-1]]
        res = 0

        def isValid(r,c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            if (r,c) in seen:
                return False
            return True


        while heap:
            h,x,y = heapq.heappop(heap)

            if x == R - 1 and y == C - 1:
                return h

            if (x,y) in seen:
                continue
            
            seen.add((x,y))
            
            for dr,dc in directions:
                nR,nC = x + dr, y + dc

                if isValid(nR, nC):
                    limit = max(h, grid[nR][nC])
                    heapq.heappush(heap, (limit, nR, nC))

            
        
        return -1
            




        