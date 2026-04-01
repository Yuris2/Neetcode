import collections

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        seen = set()

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if (r,c) in seen or grid[r][c] == 1:
                return False
            return True
            
        R,C = len(grid), len(grid[0])

        queue = deque()

        queue.append((0,0,0))
        seen.add((0,0))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while queue:
            for _ in range(len(queue)):
                r,c,steps = queue.popleft()

                if r == R - 1 and c == C - 1:
                    return steps
                
                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc

                    if isValid(newR, newC):
                        queue.append((newR,newC, steps + 1))
                        seen.add((newR, newC))
        return -1
                


        