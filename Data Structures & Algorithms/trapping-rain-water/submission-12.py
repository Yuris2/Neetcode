class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        leftHeight = [0] * n
        rightHeight = [0] * n
        lMax = 0
        rMax = 0

        for i in range(n):
            j = -i - 1
            leftHeight[i] = lMax
            rightHeight[j] = rMax

            lMax = max(lMax, heights[i])
            rMax = max(rMax, heights[j])



        
        res = 0
        for i in range(n):
            minHeight = min(leftHeight[i], rightHeight[i])
            res += max(0, minHeight - heights[i])
        
        return res


        