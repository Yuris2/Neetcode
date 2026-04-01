class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i,h in enumerate(heights):
            backfill = i
            while stack and stack[-1][0] >= h:
                height, index = stack.pop()
                area = height * (i - index)
                res = max(res,area)
                backfill = index
            stack.append((h,backfill))
        
        while stack:
            height, index = stack.pop()
            area = height * (len(heights) - index)
            res = max(res, area)
        
        return res



        