class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l,r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        res = 0

        while l < r:
            #Will spill over on the left
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                #Greater heights will get absorbed into max
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        
        return res
        