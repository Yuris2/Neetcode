class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            back = i

            while stack and stack[-1][0] >= h:
                height, index = stack.pop()
                res = max(res, (i - index) * height)
                back = index
            
            stack.append((h, back))
        
        end = len(heights)
        while stack:
            h, i = stack.pop()
            res = max(res, (end - i) * h)
        
        return res
        