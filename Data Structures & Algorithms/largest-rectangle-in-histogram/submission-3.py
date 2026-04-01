class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        stack = []

        for i in range(n):
            height = heights[i]
            store = i

            while stack and height < stack[-1][0]:
                h,j = stack.pop()
                area = h * (i - j)
                res = max(area, res)
                store = j
            
            stack.append([height, store])
        
        while stack:
            h, i = stack.pop()
            area = h * (n - i)
            res = max(area, res)
        
        return res
        