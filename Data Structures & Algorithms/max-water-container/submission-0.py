class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l < r:
            length = r - l
            height = min(heights[l], heights[r])

            area = length * height

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            maxArea = max(maxArea, area)
        
        return maxArea

            
        