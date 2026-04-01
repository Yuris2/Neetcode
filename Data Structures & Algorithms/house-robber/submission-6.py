class Solution:
    def rob(self, nums: List[int]) -> int:
        #two choices, we can rob house1 by not the adjacent house
        #We can rob the adjacent house, and skip current house
        cache = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
        
            #Rob house 1
            choice1 = nums[i] + dfs(i + 2)
            #Rob hosue 2
            choice2 = dfs(i + 1)

            cache[i] = max(choice1, choice2)

            return cache[i]

        return dfs(0)
        