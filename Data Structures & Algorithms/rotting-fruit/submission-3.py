class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Approach
        #1. Count the number of fresh and keep track of rotten fruits and time
        #2. Check each rotten fruit. Make adjacent fresh fruits rotten.
        #3. everytime you check each rotten fruit. one cycle is run
        #3. everytime a fresh fruit turns rotten decrement number of fresh
        #4. if we cannot make all fresh fruit rotten, return -1. else time
        queue = []
        fresh = 0
        time = 0

        R = len(grid)
        C = len(grid[0])

        #1.
        for r in range(R):
            for c in range(C):
                #fresh
                if grid[r][c] == 1:
                    fresh += 1
                #rotten
                elif grid[r][c] == 2:
                #keep track of rotten fruits
                    queue.append([r,c])
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        #2. 
        while queue and fresh > 0:
            n = len(queue)

            for i in range(n):
                #check rotten fruit
                row, column = queue.pop(0)
                #check adjacent 
                for dr, dc in directions:
                    adjR = row + dr
                    adjC = column + dc

                    if adjR < 0 or adjC < 0 or adjR >= R or adjC >= C or grid[adjR][adjC] != 1:
                        continue
                    #fresh turned rotten
                    fresh -= 1
                    grid[adjR][adjC] = 2
                    #rotten will be checked later
                    queue.append([adjR, adjC])
            #time elapsed by one
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1


        