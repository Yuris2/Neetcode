class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        res = 0

        for i in range(n):
            height = heights[i]
            store = i

            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                w = i - j
                area = w * h
                res = max(area, res)
                store = j

            stack.append([height, store])
        
        while stack:
            h, j = stack.pop()
            area = h * (n - j)
            res = max(res, area)
        
        return res
        