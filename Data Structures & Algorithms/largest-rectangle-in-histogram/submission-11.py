class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0 
        stack = []

        for i, height in enumerate(heights):
            backfill = i
            while stack and height < stack[-1][0]:
                h, index = stack.pop()
                backfill = index
                res = max(res, h * (i - index))
            stack.append([height, backfill])
        
        while stack:
            height, index = stack.pop()
            res = max(res, height * ((len(heights)) - index))
        return res
        