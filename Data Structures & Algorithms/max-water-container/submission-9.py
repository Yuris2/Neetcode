class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            length = (r - l)
            height = min(heights[l], heights[r])

            maxArea = max(maxArea, length * height)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
        