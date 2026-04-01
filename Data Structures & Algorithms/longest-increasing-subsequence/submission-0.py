class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        #Sequencve that can be derived by deleting some or no elements
        #Without changing the relative order
        def dfs(i, prevValue):
            #Can't increase the subsequence anymore
            if i >= len(nums):
                return 0
            if (i, prevValue) in cache:
                cache[(i, prevValue)]
            
            #Choices
            res = 0
            #1. We can include the currentValue in our subsequence, but has to be less than prevValue
            if prevValue < nums[i]:
                res = 1 + dfs(i + 1, nums[i])
            #2. We can skip the currentValue in our subsequence
            res = max(res, dfs(i + 1, prevValue))

            cache[(i, prevValue)] = res

            return res
        
        return dfs(0,-2e9)
            
        