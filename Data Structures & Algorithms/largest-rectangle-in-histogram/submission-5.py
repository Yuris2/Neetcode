class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        stack = []

        for i in range(n):
            store = i
            h = heights[i]

            while stack and  h < stack[-1][0]:
                tH, idx = stack.pop()
                #calc area in function
                maxArea = max(maxArea, (i - idx) * tH)
                store = idx
            
            stack.append([h, store])
        
        #everything left
        while stack:
            h, i = stack.pop()
            maxArea = max(maxArea, (n - i) * h)
        
        return maxArea



        