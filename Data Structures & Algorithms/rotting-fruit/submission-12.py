import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        seen = set()
        q = deque()

        fresh = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    seen.add((r,c))
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        res = 0

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if (r,c) in seen or grid[r][c] != 1:
                return False
            return True 

        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nR,nC = dr + r, dc + c
                    if isValid(nR,nC):
                        fresh -= 1
                        q.append((nR, nC))
                        seen.add((nR,nC))
        
            res += 1
        
        if fresh > 0:
            return -1
        return res



        