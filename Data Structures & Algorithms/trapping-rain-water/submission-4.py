class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        lWall = [0] * n
        rWall = [0] * n

        lMax, rMax = 0,0
        for i in range(n):
            j = -i - 1
            lWall[i] = lMax
            rWall[j] = rMax

            lMax = max(lMax, height[i])
            rMax = max(rMax, height[j])
        
        for i in range(n):
            pot = min(lWall[i], rWall[i])
            res += max(0, pot - height[i])
        
        return res