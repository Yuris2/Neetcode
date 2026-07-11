class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i,h in enumerate(heights):
            back = i

            while stack and stack[-1][0] >= h:
                height, idx = stack.pop()
                area = (i - idx) * height
                res = max(area, res)
                back = idx
            
            stack.append((h, back))
        
        r = len(heights)

        while stack:
            h, i = stack.pop()
            res = max(h* (r - i), res)
        
        return res


        