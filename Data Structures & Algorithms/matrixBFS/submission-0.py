class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = []
        visited = set()
        
        #Start from top right corner
        queue.append((0,0))
        visited.add((0,0))

        length = 0
        while queue:
            #Pop the current level
            n = len(queue)
            for i in range(n):
                
                r,c = queue.pop(0)

                if r == R -1 and c == C -1:
                    return length

                directions = [[1,0], [0,1], [-1,0], [0,-1]]

                for dr, dc in directions:
                    newR = dr + r
                    newC = dc + c
                    #Out of bounds
                    if newR < 0 or newC < 0 or newR >= R or newC >= C:
                        continue
                    #If we already visited or we hit rocks
                    if (newR, newC) in visited or grid[newR][newC] == 1:
                        continue
                    
                    queue.append((newR, newC))
                    visited.add((newR, newC))
            length += 1
        
        return -1
        
        