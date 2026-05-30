class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height = the min of r and l heights
        # width = r - l

        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * (min(heights[l], heights[r]))
            res = max(res, area)
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        
        return res

