import collections
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        seen = set()
        R,C = len(grid), len(grid[0])

        def isValid(r,c):
            if r < 0 or c < 0 or c >= C or r >= R:
                return False
            if (r,c) in seen or grid[r][c] == -1:
                return False
            return True
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r,c,0))
                    seen.add((r,c))
        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        while q:
            r,c,dist = q.popleft()
            grid[r][c] = dist
            
            for dr,dc in directions:
                nR,nC = r + dr, c + dc
                if isValid(nR,nC):
                    q.append((nR,nC, dist + 1))
                    seen.add((nR,nC))
        

        


        