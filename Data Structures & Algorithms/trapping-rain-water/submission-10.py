class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lWall = [0] * n
        rWall = [0] * n

        lMax, rMax = 0,0
        #Track max height that we have seen from left and right
        for i in range(n):
            j = -i - 1
            
            lWall[i], rWall[j] = lMax, rMax
            lMax = max(lMax, height[i])
            rMax = max(rMax, height[j])
        
        res = 0
        #Iterate over the array
        for i in range(n):
            #Find the minimum height that we have seen from L,R
            pot = min(lWall[i], rWall[i])
                #Will spill over 
            res += max(0, pot - height[i])
            #Check the height of the wall:
                #Add difference to res if min height - wall > 0
        
        return res

        