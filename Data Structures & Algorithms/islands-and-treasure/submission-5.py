import collections
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R,C = len(grid), len(grid[0])
        q = deque()
        seen = set()

        def isValid(r,c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            if grid[r][c] == -1 or (r,c) in seen:
                return False
            return True

        for r in range(R):
            for c in range(C):
                #If we have a treasure chest
                if grid[r][c] == 0:
                    #Append coordinates along with dist
                    q.append((r,c,0))
                    seen.add((r,c))
        
        directions = [[1,0],[0,1], [-1,0], [0,-1]]

        while q:
            r,c,prevDistance = q.popleft()

            dist = prevDistance + 1
            for dr, dc in directions:
                new_r, new_c = dr + r, dc + c

                if isValid(new_r, new_c):
                    grid[new_r][new_c] = dist
                    q.append((new_r, new_c, dist))
                    seen.add((new_r,new_c))




        