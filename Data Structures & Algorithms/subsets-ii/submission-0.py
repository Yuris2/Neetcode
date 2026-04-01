class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(stack.copy())
                return 
            
            stack.append(nums[i])
            dfs(i + 1)
            stack.pop()

            #Duplicates occur when we run into the same elements at the same level
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)
        
        dfs(0)
        return res
        