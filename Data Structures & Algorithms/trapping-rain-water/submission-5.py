class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        #max height we have seen from the leftside
        lWall = [0] * n
        #max height we have seen from the rightside
        rWall = [0] * n
        res = 0

        lMax,rMax = 0,0
        #populate heights
        for i in range(n):
            j = -i - 1

            lWall[i] = lMax
            rWall[j] = rMax

            lMax = max(height[i], lMax)
            rMax = max(height[j], rMax)

        for i in range(n):
            pot = min(lWall[i], rWall[i])
            res += max(0, pot - height[i])
        
        return res
        #go throgh the array
        #calculate potential height
        #check if the wall at the current index > potential
        #if not add to the res
        