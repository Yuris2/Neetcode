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
                res = max(h * (i - j), res)
                store = j
            
            stack.append([height, store])
        
        while stack:
            h, i = stack.pop()
            res = max(h * (n - i), res)
        
        return res
        