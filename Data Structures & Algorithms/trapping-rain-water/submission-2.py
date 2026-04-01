class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        res = 0

        lMax, rMax = 0,0 
        for i in range(n):
            j = -i - 1

            left[i] = lMax
            right[j] = rMax

            lMax = max(lMax, height[i])
            rMax = max(rMax, height[j])

        
        for i in range(n):
            pot = min(left[i], right[i])
            res += max(0, pot - height[i])
        
        return res

        
        



            
        