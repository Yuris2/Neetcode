class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, height in enumerate(heights):
            backFill = i
            while stack and height < stack[-1][0]:
                h, idx = stack.pop()
                area = h * (i - idx)
                res = max(res, area)
                backFill = idx
            stack.append([height, backFill])
        
        while stack:
            height, index = stack.pop()
            area = height * (len(heights) - index)
            res = max(area, res)
        
        return res



        