class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])

            largestArea = max(area, largestArea)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return largestArea


        