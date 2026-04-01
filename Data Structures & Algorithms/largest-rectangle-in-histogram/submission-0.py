class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n):
            height = heights[i]
            #Flood starts at current index
            store = i
            #Monotomic Stack thing. 
            #While stack is not empty and the height is less than top of stack
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                w = i - j
                area = h * w
                maxArea = max(maxArea, area)
                #Height floods backwards until the height at top is less
                store = j
                
            stack.append([height, store])
        
        #Stack is not going to be empty atm. Calculate area to end of wall
        while stack:
            w = n
            h, i = stack.pop()
            area = h * (n - i)
            maxArea = max(area, maxArea)
        
        return maxArea

        