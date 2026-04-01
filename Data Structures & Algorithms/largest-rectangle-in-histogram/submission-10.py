class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, height in enumerate(heights):
            back = i
            while stack and height < stack[-1][0]:
                h, idx = stack.pop()
                area = h * (i - idx)
                res = max(area, res)
                back = idx
            stack.append([height, back])
        
        while stack:
            h, i = stack.pop()
            res = max(res, h * (len(heights) - i))
        
        return res
        
        
        