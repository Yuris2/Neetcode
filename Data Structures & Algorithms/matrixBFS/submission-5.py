import collections

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        seen = set()
        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if (r,c) in seen or grid[r][c] == 1:
                return False
            return True

        queue = deque()
        queue.append([0,0,0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        seen.add((0,0))

        while queue:
            for _ in range(len(queue)):
                r,c,steps = queue.popleft()

                if r == R - 1 and c == C - 1:
                    return steps
                
                for dr,dc in directions:
                    new_r = dr + r
                    new_c = dc + c

                    if isValid(new_r, new_c):
                        queue.append([new_r, new_c, steps + 1])
                        seen.add((new_r,new_c))

        return -1

        