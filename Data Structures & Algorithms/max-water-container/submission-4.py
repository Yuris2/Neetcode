class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            length = r - l

            area = height * length
            largestArea = max(area, largestArea)
            #Conditional check
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return largestArea
        