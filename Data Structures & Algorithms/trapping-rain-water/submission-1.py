class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        rWall = [0] * n
        lWall = [0] * n

        rMax, lMax = 0,0
        #Populating Heights
        for i in range(n):
            j = -i - 1
            lWall[i] = lMax
            rWall[j] = rMax

            lMax = max(height[i], lMax)
            rMax = max(height[j], rMax)
        
        res = 0 
        for i in range(n):
            pot = min(rWall[i], lWall[i])
            res += max(0, pot - height[i])

        return res
        