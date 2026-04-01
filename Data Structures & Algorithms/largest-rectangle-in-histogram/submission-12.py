class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Have a stack store each (height, index)
        stack = []
        res = 0

        #Iterate through each height and index:
        for i, h in enumerate(heights):
            backFill = i
            #While the current height < height at the top of the stack (h2)
            while stack and h < stack[-1][0]:
                #pop from the stack and calculate the area from h2
                h2, i2 = stack.pop()
                area = h2 * (i - i2)
                #our index can spill backwards so we need to track back
                backFill = i2
                #calculate max res
                res = max(res, area)
            #Append (height, index) to stack
            stack.append((h,backFill))

        #Empty out stack and calculate area
        n = len(heights)
        while stack:
            h,i = stack.pop()
            res = max(res, h * (n - i))
        
        return res


        