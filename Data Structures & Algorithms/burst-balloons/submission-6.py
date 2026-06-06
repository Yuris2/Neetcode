class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #Pattern:
            #2D-DP where array is changing in size for each decision
        #General Idea
            #Flip problem around to find last balloon to pop
            #Track last neighbors with l,r pointers
            #Each layer, calculate popping which balloon gives the highest value

        nums = [1] + nums + [1]
        cache = {}
        def dp(l,r):
            if l > r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            
            res = 0

            #Iterate over the unpopped balloons
            for i in range(l + 1, r):
                #Value of current balloon being popped
                val = nums[l] * nums[i] * nums[r]
                #Adding the res of the other layers
                val += dp(l,i) + dp(i,r)
                res = max(res, val)
            
            cache[(l,r)] = res
            return res
        
        return dp(0, len(nums) - 1)
        