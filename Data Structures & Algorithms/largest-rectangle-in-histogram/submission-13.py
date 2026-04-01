class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #We have heights and an index
        #We can use indices to track the width of a certain rectangle
        #A rectangle's height can go backward
        #At every index, we want to see how far a rectangle can spill over
            #The height has to be less than the current position
        n = len(heights)
        stack = []
        maxArea = 0

        for idx, height in enumerate(heights):
            backFill = idx
            while stack and height < stack[-1][0]:
                #The current rectangle can't extend
                h,i = stack.pop()
                #Calculate max area from certain rectangle
                length = idx - i
                maxArea = max(maxArea, h * length)
                backFill = i
            
            stack.append([height, backFill])
        
        while stack:
            height, index = stack.pop()
            maxArea = max(maxArea, height * (n - index))
        
        return maxArea
            

