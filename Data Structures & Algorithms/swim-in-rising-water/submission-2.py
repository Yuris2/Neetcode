import collections
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Water level is rising 
        #You can swim to the next square if:
            #Original Elevation of both Squares <= water level at t
        #Start at (0,0) return minumum amount of time to reach bottom right

        #Solution
            #Find the shortest path between the top left and bottom right with respect to time
            #BFS is good for finding shortest path of unweighted nodes
            #Since nodes have a weight with respect to elevation
                #Djikstras (current_cost, (coord))
                    #Current Cost Represents the max cost to get from the top left to point
            #Keep track of where water is in respect to the grid
        R,C = len(grid), len(grid[0])
        goal = (R - 1, C - 1)
        seen = set([(0,0)])
        minHeap = [[grid[0][0], (0,0)]]

        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if (r,c) in seen:
                return False
            return True

        while minHeap:
            curr, point = heapq.heappop(minHeap)

            if point == goal:
                return curr
            
            r,c = point

            for dr, dc in directions:
                new_r, new_c = dr + r, dc + c
                if isValid(new_r, new_c):
                    seen.add((new_r,new_c))
                    cost = max(curr, grid[new_r][new_c])
                    heapq.heappush(minHeap, (cost, (new_r, new_c)))
        
        return -1
        