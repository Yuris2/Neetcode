class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        cache = {}
        target = sum(nums) // 2
        
        def dp(i, t):
            if t == target:
                return True
            if i >= len(nums) or t > target:
                return False
            if (i,t) in cache:
                return cache[(i,t)]
            
            cache[(i,t)] =  dp(i + 1, t + nums[i]) or dp(i + 1, t)
            return cache[(i,t)]
        
        return dp(0,0)
        