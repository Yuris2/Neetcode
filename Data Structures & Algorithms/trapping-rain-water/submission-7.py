class Solution:
    def trap(self, height: List[int]) -> int:
        #Max height of water we before a given index
        #l = [0,0,2,2,3,3,3,3,3,3]
        #r = [3,3,3,3,3,3,3,2,1,0]

        #h = [0,2,0,3,1,0,1,3,2,1]

        #res=[0,0,2,0,2,3,2,0,0,0]

        lWall = [0] * len(height)
        rWall = [0] * len(height)

        lMax, rMax = 0,0
        for i in range(len(height)):
            j = -i - 1

            lWall[i] = lMax
            rWall[j] = rMax

            lMax = max(height[i],lMax)
            rMax = max(height[j],rMax)

        res = 0
        for i in range(len(height)):
            pot = min(lWall[i],rWall[i])
            res += max(0, pot - height[i])
        
        return res



        