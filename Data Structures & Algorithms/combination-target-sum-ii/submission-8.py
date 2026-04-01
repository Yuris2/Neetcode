class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        stack = []

        def dp(i, total):
            if total == target:
                res.append(stack.copy())
                return
            if i >= len(nums):
                return
            
            stack.append(nums[i])
            dp(i + 1, total + nums[i])

            stack.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            dp(i + 1, total)
        
        dp(0,0)
        return res

        