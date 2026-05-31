class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i,h in enumerate(heights):
            backfill = i
            #Maintain a monotonic stack where height is increasing
            while stack and stack[-1][0] > h:
                height, idx = stack.pop()
                area = height * (i - idx)
                res = max(area, res)
                backfill = idx

            stack.append((h,backfill))
        
        n = len(heights)
        while stack:
            height, idx = stack.pop()
            area = height * (n - idx)
            res = max(area, res)
        
        return res
        