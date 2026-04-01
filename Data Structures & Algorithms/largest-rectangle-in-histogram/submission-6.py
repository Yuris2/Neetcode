class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        stack = []

        for i in range(len(heights)):
            height = heights[i]
            spill = i

            while stack and height < stack[-1][0]:
                val, ind = stack.pop()
                area = (i - ind) * val
                res = max(area, res)
                spill = ind
            
            stack.append([height, spill])
        
        while stack:
            val, ind = stack.pop()
            res = max(res, (n - ind) * val)
        
        return res
        