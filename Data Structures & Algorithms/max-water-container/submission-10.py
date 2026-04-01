class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        l = 0
        r = len(heights) - 1

        while l < r:
            base = r - l
            height = min(heights[l], heights[r])

            res = max(res, base * height)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
        