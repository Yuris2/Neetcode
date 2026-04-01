class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        res = 0

        while l < r:
            height = min(heights[l], heights[r])
            length = (r - l)

            res = max(res, height * length)
        
            #Move the limiting height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
        