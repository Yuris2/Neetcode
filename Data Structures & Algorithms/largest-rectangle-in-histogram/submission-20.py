class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        res = 0
        for i,h in enumerate(heights):
            back = i

            while stack and stack[-1][0] > h:
                height, idx = stack.pop()
                area = height * (i - idx)
                res = max(area, res)

                back = idx
            
            stack.append((h,back))
        
        n = len(heights)

        while stack:
            h,i = stack.pop()
            area = h * (n - i)
            res = max(area, res)
        
        return res

        