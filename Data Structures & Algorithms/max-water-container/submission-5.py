class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l = 0 
        r = len(heights) - 1

        while l < r:
            area = min(heights[r], heights[l]) * (r - l)
            res = max(res, area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return res
        