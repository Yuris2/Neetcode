class Solution:
    def trap(self, height: List[int]) -> int:
        #We want to find the max height of water we can store at 
        #a given index by checking the maxHeight we have seen from 
        #the left and the right
        lWall = [0] * len(height)
        rWall = [0] * len(height)

        lMax, rMax = 0,0
        #Constructing arrays of the maxHeight that we have seen from
        for i in range(len(height)):
            j = -i - 1

            lWall[i] = lMax
            rWall[j] = rMax

            lMax = max(lMax, height[i])
            rMax = max(rMax, height[j])
        #left of given index and right of given index
        #height of water that we can potentially store is the min height
        #b/c water will spill over 
        res = 0
        for i in range(len(height)):
            pot = min(lWall[i], rWall[i])
            res += max(0, pot - height[i])
        return res
        #Then calculate the total height by subtracting the actual wall 
        #Height at given index
    