import collections

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        seen = set()
        def isValid(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return False
            if (r,c) in seen or grid[r][c] == 1:
                return False
            return True
        
        queue = deque()
        queue.append((0,0,0))
        seen.add((0,0))

        directions = [[1,0],[0,-1],[0,1],[-1,0]]
        while queue:
            for i in range(len(queue)):
                r,c,path = queue.popleft()

                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return path
                
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if isValid(new_r, new_c):
                        queue.append((new_r, new_c, path + 1))
                        seen.add((new_r, new_c))
                
        
        return -1


        