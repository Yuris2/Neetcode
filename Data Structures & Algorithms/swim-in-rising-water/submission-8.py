import collections
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        seen = {(0,0)}
        heap = [(grid[0][0], 0, 0)]

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        goal = (R - 1, C - 1)

        def isValid(r,c):
            if r < 0 or r >= R or c >= C or c < 0:
                return False
            if (r,c) in seen:
                return False
            return True

        while heap:
            time, r, c = heapq.heappop(heap)

            if (r,c) == goal:
                return time
            
            for dr, dc in directions:
                nR, nC = r + dr, c + dc

                if isValid(nR, nC):
                    cost = max(time, grid[nR][nC])
                    seen.add((nR, nC))
                    heapq.heappush(heap, (cost, nR, nC))
        
        return -1
        