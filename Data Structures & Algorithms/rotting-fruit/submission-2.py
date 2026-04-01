class Solution:
    def orangesRotting(self, nums):
        ROWS = len(nums)
        COL = len(nums[0])

        fresh = 0
        time = 0
        queue = []

        for r in range(ROWS):
            for c in range(COL):
                if nums[r][c] == 1:
                    fresh += 1
                elif nums[r][c] == 2:
                    queue.append([r,c])
        
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        while queue and fresh > 0:
            n = len(queue)

            for i in range(len(queue)):
                row, column = queue.pop(0)

                #Check every coordinate arround it

                for dr, dc in directions:
                    r = row + dr
                    c = column + dc

                    if r < 0 or r >= ROWS or c < 0 or c >= COL or nums[r][c] != 1:
                        continue

                    fresh -= 1
                    nums[r][c] = 2
                    queue.append([r,c])
                
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1

        