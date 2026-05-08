class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        goal = (R - 1, C - 1)

        minHeap = [(grid[0][0],0,0)]
        seen = {(0,0)}
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if (r,c) in seen:
                return False
            return True

        while minHeap:
            height, r, c = heapq.heappop(minHeap)

            if (r,c) == goal:
                return height
            
            for dr, dc in directions:
                nR, nC = (dr + r), (dc + c)

                if isValid(nR, nC):
                    h = max(height, grid[nR][nC])
                    heapq.heappush(minHeap, (h, nR, nC))
                    seen.add((nR, nC))
        
        return -1
        

                







        