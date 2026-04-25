import collections
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])

        start = grid[0][0]
        seen = {(0,0)}
        minHeap = [(start,0,0)]
        heapq.heapify(minHeap)

        goal = (R - 1, C - 1)
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if (r,c) in seen:
                return False
            return True

        while True:
            cost,r,c = heapq.heappop(minHeap)

            if (r,c) == goal:
                return cost 
            
            for dr, dc in directions:
                new_r, new_c = dr + r, dc + c
                if isValid(new_r, new_c):
                    cst = max(cost, grid[new_r][new_c])
                    heapq.heappush(minHeap, (cst, new_r, new_c))
                    seen.add((new_r, new_c))
        
        return -1


        