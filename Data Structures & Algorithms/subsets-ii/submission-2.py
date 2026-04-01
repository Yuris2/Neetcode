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

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            stack.pop()
            dfs(i + 1)

            return
        
        dfs(0)
        return res