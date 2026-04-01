class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lHeight = [0] * n
        rHeight = [0] * n

        lMax,rMax = 0,0

        for i in range(n):
            j = -i - 1

            lHeight[i] = lMax
            rHeight[j] = rMax

            lMax = max(lMax, height[i])
            rMax = max(rMax, height[j])
        
        res = 0
        for i in range(n):
            pot = min(rHeight[i], lHeight[i])
            res += max(0, pot - height[i])
        
        return res

        