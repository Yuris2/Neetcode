class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dp(i, prevEnd):
            if i >= len(nums):
                return 0
            if (i, prevEnd) in cache:
                return cache[(i,prevEnd)]
            
            res = 0
            #If the current number > prevEnd, start add to current sequence
            if prevEnd < nums[i]:
                res += 1 + dp(i + 1, nums[i])
            
            #Start a new sequence
            res = max(res, dp(i + 1, prevEnd))
            cache[(i,prevEnd)] = res

            return res
        
        return dp(0,-2e9)
        