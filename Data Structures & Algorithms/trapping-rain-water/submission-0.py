class Solution:
    def trap(self, heights: List[int]) -> int:
        #Approach (sweep and fill)
        #1. Find the concurring max heights of left side (only update max to left)
        #2. Find the concurring max heights of right side
        #3. Calculate overlap (min of leftHeight and right)
        #4. Return the sum of the difference between overlap and height (avoid negative heights)
    
        lWall, rWall = 0, 0
        lHeights = [0] * len(heights)
        rHeights = [0] * len(heights)
        res = 0

        for i in range(len(heights)):
            #to calculate the right pointer at the same time
            j = -i - 1
            lHeights[i] = lWall
            rHeights[j] = rWall
            lWall = max(lWall, heights[i])
            rWall = max(rWall, heights[j])
        
        for i in range(len(heights)):
            #3
            newHeight = min(lHeights[i], rHeights[i])
            #ensuring that it is not negative
            res += max(0, newHeight - heights[i])
        
        return res
        

        

        

        