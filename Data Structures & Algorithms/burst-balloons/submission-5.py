class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #Want to think about the last balloon we pop
        nums = [1] + nums + [1]
        cache = {}
        #Track the interval of possible balloons (l,r):
        def dp(l,r):
            if l > r:
            #When the interval is closed (l > r):
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            res = 0
            #Iterate through unpopped balloons
            for i in range(l + 1,r):
                #Pop that balloon
                c = nums[l] * nums[i] * nums[r]
                #Add the result of popping balloons before that balloon
                c += dp(l,i) + dp(i,r)
                res = max(res, c)
            cache[(l,r)] = res
            return res
        

        return dp(0, len(nums) - 1)
        