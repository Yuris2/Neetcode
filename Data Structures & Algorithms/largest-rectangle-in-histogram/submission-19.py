class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = -2e9

        for i,h in enumerate(heights):
            backfill = i

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                area = height * (i - idx)
                res = max(area, res)

                backfill = idx
            
            stack.append((backfill, h))
        
        n = len(heights)

        while stack:
            i,h=stack.pop()
            res = max(res, h * (n - i))

        return res

            

        