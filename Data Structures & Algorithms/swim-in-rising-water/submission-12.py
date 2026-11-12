import collections
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        R,C = len(grid), len(grid[0])
        seen = set()

        heapq.heappush(heap, (grid[0][0], 0, 0))
        res = 0
        directions = [[1,0],[0,1],[-1,0], [0,-1]]

        def isValid(r,c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            if (r,c) in seen:
                return False
            return True

        while heap:
            height, r, c = heapq.heappop(heap)


            if r == R - 1 and c == C - 1:
                return height
            if (r,c) in seen:
                continue
                
            seen.add((r, c))
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if isValid(nr, nc):
                    h = max(grid[nr][nc], height)
                    heapq.heappush(heap, (h, nr, nc))
                        
        
        return -1

        